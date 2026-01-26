
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Multiple Windows")
        button = QPushButton('Open Secondary Window')
        button.clicked.connect(self.open_window)
        
        self.setCentralWidget(button)

        self.count = 1
        self.window = []


    def open_window(self):
        w = SecondaryWindow(self.count)
        self.count += 1

        self.window.append(w)

        w.show()


class SecondaryWindow(QMainWindow):
    def __init__(self,n):
        super().__init__()
        self.setWindowTitle('Window Number n')

        label = QLabel(f"Number: {n}")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
