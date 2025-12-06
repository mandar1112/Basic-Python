import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import yt_dlp
import threading
import os
import subprocess
from PIL import Image, ImageTk
import io
import requests

class YouTubeDownloader:
    def __init__(self):
        self.download_cancelled = False
        self.has_ffmpeg = self.check_ffmpeg()
        self.thumbnail_image = None
        self.start_time = None
        self.downloaded_bytes = 0
        
    def check_ffmpeg(self):
        """Check if FFmpeg is installed"""
        try:
            subprocess.run(['ffmpeg', '-version'], 
                         capture_output=True, 
                         check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
        
    def progress_hook(self, d):
        """Update progress bar and speed during download"""
        if d['status'] == 'downloading':
            if 'total_bytes' in d:
                total = d['total_bytes']
                downloaded = d['downloaded_bytes']
                percentage = (downloaded / total) * 100
            elif 'total_bytes_estimate' in d:
                total = d['total_bytes_estimate']
                downloaded = d['downloaded_bytes']
                percentage = (downloaded / total) * 100
            else:
                percentage = 0
            
            # Calculate download speed
            speed = d.get('speed')
            if speed:
                speed_mb = speed / (1024 * 1024)
                speed_text = f"{speed_mb:.2f} MB/s"
            else:
                speed_text = "Calculating..."
            
            # Calculate ETA
            eta = d.get('eta')
            if eta:
                eta_text = f"ETA: {eta}s"
            else:
                eta_text = ""
            
            progress_bar['value'] = percentage
            progress_label.config(text=f"{percentage:.1f}% - {speed_text} {eta_text}")
            window.update_idletasks()
        
        elif d['status'] == 'finished':
            progress_bar['value'] = 100
            progress_label.config(text="100% - Processing...")
            window.update_idletasks()

    def load_thumbnail(self, url):
        """Load and display video thumbnail"""
        try:
            response = requests.get(url, timeout=5)
            image_data = response.content
            image = Image.open(io.BytesIO(image_data))
            
            # Resize thumbnail to fit
            image.thumbnail((200, 150))
            
            photo = ImageTk.PhotoImage(image)
            thumbnail_label.config(image=photo)
            thumbnail_label.image = photo
        except Exception as e:
            thumbnail_label.config(text="No thumbnail", image='')

    def fetch_video_info(self):
        """Fetch and display video information"""
        try:
            url = url_entry.get().strip()
            if not url:
                messagebox.showerror("Error", "Please enter a YouTube URL")
                return

            status_label.config(text="Fetching video info...", fg="blue")
            info_label.config(text="")
            resolution_combo.set("")
            resolution_combo['values'] = []
            thumbnail_label.config(image='', text="Loading...")
            window.update()

            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                # Display video info
                duration_min = info['duration'] // 60
                duration_sec = info['duration'] % 60
                title = info['title'][:50] + "..." if len(info['title']) > 50 else info['title']
                uploader = info.get('uploader', 'Unknown')
                view_count = info.get('view_count', 0)
                views_formatted = f"{view_count:,}" if view_count else "N/A"
                
                info_text = f"Title: {title}\nUploader: {uploader}\nDuration: {duration_min}:{duration_sec:02d} | Views: {views_formatted}"
                info_label.config(text=info_text)
                
                # Load thumbnail
                thumbnail_url = info.get('thumbnail')
                if thumbnail_url:
                    threading.Thread(target=self.load_thumbnail, args=(thumbnail_url,), daemon=True).start()
                
                # Get available formats
                formats = []
                seen_resolutions = set()
                
                if self.has_ffmpeg:
                    # With FFmpeg: can merge separate video+audio for best quality
                    for f in info['formats']:
                        if f.get('vcodec') != 'none' and f.get('height') is not None:
                            height = f.get('height')
                            if height not in seen_resolutions and height >= 144:
                                ext = f.get('ext', 'mp4')
                                formats.append((height, f"{height}p - {ext.upper()}"))
                                seen_resolutions.add(height)
                else:
                    # Without FFmpeg: only pre-merged formats
                    for f in info['formats']:
                        if (f.get('vcodec') != 'none' and 
                            f.get('acodec') != 'none' and 
                            f.get('height') is not None):
                            height = f.get('height')
                            ext = f.get('ext', 'mp4')
                            if height not in seen_resolutions and height >= 144:
                                formats.append((height, f"{height}p - {ext.upper()}"))
                                seen_resolutions.add(height)
                
                # Sort by quality (highest first)
                formats.sort(reverse=True, key=lambda x: x[0])
                resolution_list = [f[1] for f in formats]
                
                # Add audio-only option
                resolution_list.append("Audio Only (MP3)")
                
                if not resolution_list:
                    resolution_list = ["Best Available Quality"]
                
                resolution_combo['values'] = resolution_list
                resolution_combo.current(0)
                download_btn.config(state="normal")
                playlist_btn.config(state="normal")
                subtitle_check.config(state="normal")
                
                if self.has_ffmpeg:
                    status_label.config(text="Ready to download (FFmpeg detected ✓)", fg="green")
                else:
                    status_label.config(text="Ready (Limited quality - FFmpeg not found)", fg="orange")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch video info:\n{str(e)}")
            status_label.config(text="Error", fg="red")

    def download_video_thread(self):
        """Download video in separate thread"""
        try:
            url = url_entry.get().strip()
            if not url:
                messagebox.showerror("Error", "Please enter a YouTube URL")
                return

            path = filedialog.askdirectory()
            if not path:
                return

            # Disable buttons during download
            download_btn.config(state="disabled")
            fetch_btn.config(state="disabled")
            playlist_btn.config(state="disabled")

            selected = resolution_combo.get()
            download_subtitles = subtitle_var.get()
            
            # Configure download options
            ydl_opts = {
                'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
                'progress_hooks': [self.progress_hook],
            }
            
            # Add subtitle options
            if download_subtitles:
                ydl_opts['writesubtitles'] = True
                ydl_opts['writeautomaticsub'] = True
                ydl_opts['subtitleslangs'] = ['en']
            
            # Check if audio-only download
            if "Audio Only" in selected:
                ydl_opts['format'] = 'bestaudio/best'
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
                if not self.has_ffmpeg:
                    messagebox.showwarning("Warning", "FFmpeg is required for audio extraction.\nDownloading best audio format instead.")
                    ydl_opts['postprocessors'] = []
            else:
                # Video download
                if selected and "Best Available Quality" not in selected:
                    height = selected.split('p')[0]
                    if self.has_ffmpeg:
                        ydl_opts['format'] = f'bestvideo[height<={height}]+bestaudio/best[height<={height}]'
                        ydl_opts['merge_output_format'] = 'mp4'
                    else:
                        ydl_opts['format'] = f'best[height<={height}]'
                else:
                    if self.has_ffmpeg:
                        ydl_opts['format'] = 'bestvideo+bestaudio/best'
                        ydl_opts['merge_output_format'] = 'mp4'
                    else:
                        ydl_opts['format'] = 'best'

            status_label.config(text="Downloading...", fg="blue")
            progress_bar['value'] = 0
            window.update()

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            progress_bar['value'] = 100
            progress_label.config(text="100%")
            status_label.config(text="Download Complete!", fg="green")
            messagebox.showinfo("Success", f"Download completed successfully!\n\nLocation:\n{path}")

        except Exception as e:
            messagebox.showerror("Error", f"Download failed:\n{str(e)}")
            status_label.config(text="Download failed", fg="red")
        
        finally:
            # Re-enable buttons
            download_btn.config(state="normal")
            fetch_btn.config(state="normal")
            playlist_btn.config(state="normal")
            progress_bar['value'] = 0
            progress_label.config(text="")

    def download_playlist_thread(self):
        """Download entire playlist"""
        try:
            url = url_entry.get().strip()
            if not url:
                messagebox.showerror("Error", "Please enter a YouTube URL")
                return

            # Check if it's a playlist
            if 'playlist' not in url and 'list=' not in url:
                messagebox.showwarning("Warning", "This doesn't appear to be a playlist URL.\nUse 'Download Video' for single videos.")
                return

            path = filedialog.askdirectory()
            if not path:
                return

            # Disable buttons
            download_btn.config(state="disabled")
            fetch_btn.config(state="disabled")
            playlist_btn.config(state="disabled")

            selected = resolution_combo.get()
            download_subtitles = subtitle_var.get()
            
            ydl_opts = {
                'outtmpl': os.path.join(path, '%(playlist_index)s - %(title)s.%(ext)s'),
                'progress_hooks': [self.progress_hook],
                'ignoreerrors': True,  # Continue on errors
            }
            
            if download_subtitles:
                ydl_opts['writesubtitles'] = True
                ydl_opts['writeautomaticsub'] = True
                ydl_opts['subtitleslangs'] = ['en']
            
            # Format selection
            if "Audio Only" in selected:
                ydl_opts['format'] = 'bestaudio/best'
                if self.has_ffmpeg:
                    ydl_opts['postprocessors'] = [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }]
            else:
                if self.has_ffmpeg:
                    ydl_opts['format'] = 'bestvideo+bestaudio/best'
                    ydl_opts['merge_output_format'] = 'mp4'
                else:
                    ydl_opts['format'] = 'best'

            status_label.config(text="Downloading playlist...", fg="blue")
            progress_bar['value'] = 0
            window.update()

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            status_label.config(text="Playlist Download Complete!", fg="green")
            messagebox.showinfo("Success", f"Playlist downloaded successfully!\n\nLocation:\n{path}")

        except Exception as e:
            messagebox.showerror("Error", f"Playlist download failed:\n{str(e)}")
            status_label.config(text="Download failed", fg="red")
        
        finally:
            download_btn.config(state="normal")
            fetch_btn.config(state="normal")
            playlist_btn.config(state="normal")
            progress_bar['value'] = 0
            progress_label.config(text="")

    def download_video(self):
        """Start video download in separate thread"""
        thread = threading.Thread(target=self.download_video_thread, daemon=True)
        thread.start()

    def download_playlist(self):
        """Start playlist download in separate thread"""
        thread = threading.Thread(target=self.download_playlist_thread, daemon=True)
        thread.start()

# Initialize downloader
downloader = YouTubeDownloader()

# GUI Window
window = tk.Tk()
window.title("YouTube Downloader Pro")
window.geometry("600x580")
window.resizable(False, False)
window.configure(bg="#f0f0f0")

# Title
title_label = tk.Label(window, text="YouTube Downloader Pro", 
                       font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#1a73e8")
title_label.pack(pady=10)

# FFmpeg Status
ffmpeg_status = "FFmpeg: ✓ Installed" if downloader.has_ffmpeg else "FFmpeg: ⚠️ Not Found"
ffmpeg_color = "green" if downloader.has_ffmpeg else "orange"
ffmpeg_label = tk.Label(window, text=ffmpeg_status, 
                       font=("Arial", 9), bg="#f0f0f0", fg=ffmpeg_color)
ffmpeg_label.pack()

# URL Entry Frame
url_frame = tk.Frame(window, bg="#f0f0f0")
url_frame.pack(pady=8)

url_label = tk.Label(url_frame, text="YouTube URL:", 
                     font=("Arial", 11), bg="#f0f0f0")
url_label.pack()

url_entry = tk.Entry(url_frame, width=60, font=("Arial", 10))
url_entry.pack(pady=5)

# Fetch Button
fetch_btn = tk.Button(window, text="📥 Fetch Info", font=("Arial", 11), 
                     bg="#2196F3", fg="white", command=downloader.fetch_video_info,
                     cursor="hand2", relief="flat", padx=20, pady=5)
fetch_btn.pack(pady=5)

# Thumbnail and Info Frame
content_frame = tk.Frame(window, bg="#f0f0f0")
content_frame.pack(pady=5)

# Thumbnail
thumbnail_label = tk.Label(content_frame, text="Thumbnail will appear here", 
                          bg="#e0e0e0", width=25, height=8, relief="solid", borderwidth=1)
thumbnail_label.pack(side="left", padx=10)

# Video Info
info_label = tk.Label(content_frame, text="", font=("Arial", 9), 
                     bg="#f0f0f0", fg="#333", justify="left", wraplength=300)
info_label.pack(side="left", padx=5)

# Options Frame
options_frame = tk.Frame(window, bg="#f0f0f0")
options_frame.pack(pady=8)

# Resolution Selection
resolution_label = tk.Label(options_frame, text="Quality:", 
                           font=("Arial", 10), bg="#f0f0f0")
resolution_label.grid(row=0, column=0, padx=5, sticky="e")

resolution_combo = ttk.Combobox(options_frame, width=28, state="readonly")
resolution_combo.grid(row=0, column=1, padx=5)

# Subtitle Checkbox
subtitle_var = tk.BooleanVar()
subtitle_check = tk.Checkbutton(options_frame, text="Download Subtitles", 
                               variable=subtitle_var, font=("Arial", 9),
                               bg="#f0f0f0", state="disabled")
subtitle_check.grid(row=1, column=1, pady=5, sticky="w")

# Download Buttons Frame
button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack(pady=8)

download_btn = tk.Button(button_frame, text="⬇️ Download Video", font=("Arial", 11, "bold"), 
                        bg="#4CAF50", fg="white", command=downloader.download_video,
                        cursor="hand2", relief="flat", padx=20, pady=8,
                        state="disabled")
download_btn.pack(side="left", padx=5)

playlist_btn = tk.Button(button_frame, text="📋 Download Playlist", font=("Arial", 11, "bold"), 
                        bg="#FF9800", fg="white", command=downloader.download_playlist,
                        cursor="hand2", relief="flat", padx=20, pady=8,
                        state="disabled")
playlist_btn.pack(side="left", padx=5)

# Progress Bar Frame
progress_frame = tk.Frame(window, bg="#f0f0f0")
progress_frame.pack(pady=8)

progress_bar = ttk.Progressbar(progress_frame, length=500, mode='determinate')
progress_bar.pack()

progress_label = tk.Label(progress_frame, text="", font=("Arial", 9), bg="#f0f0f0")
progress_label.pack(pady=3)

# Status Label
status_label = tk.Label(window, text="Enter a URL and click 'Fetch Info'", 
                       font=("Arial", 10), bg="#f0f0f0", fg="#666")
status_label.pack(pady=5)

# Footer
if not downloader.has_ffmpeg:
    footer_text = "⚠️ Install FFmpeg for best quality & audio extraction"
else:
    footer_text = "✓ All features enabled | Audio extraction, playlists, subtitles supported"

footer_label = tk.Label(window, text=footer_text, 
                       font=("Arial", 8), bg="#f0f0f0", fg="#666")
footer_label.pack(side="bottom", pady=8)

window.mainloop()