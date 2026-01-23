# Calculator Using PySide6
import psutil
import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton
from PySide6.QtCore import Qt, QTimer



class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.first_number = ""
        self.operator = ""
        self.second_number = ""
        
        # Timer to update resource usage
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_resource_usage)
        self.timer.start(1000) # every 1 sec

        self.setWindowTitle("Calculator Made Using PySide6")
        self.setFixedSize(300,400)


        container = QWidget()
        self.setCentralWidget(container)

        # Status bar for system usage
        self.status = self.statusBar()
        self.status.showMessage("CPU: 0% | Ram: 0 MB")

        main_layout = QVBoxLayout()
        container.setLayout(main_layout)

        # Display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(60)
        self.display.setStyleSheet("font-size: 28px;")

        main_layout.addWidget(self.display)


        # Grid for buttons
        grid = QGridLayout()
        main_layout.addLayout(grid)

        buttons = [
            ('x^_', 0, 0), ('x^2', 0, 1), ('C', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('00', 4, 0), ('0', 4, 1), ('.', 4, 2), ('=', 4, 3),
        ]

        for text, row, col in buttons:
            btn = QPushButton(text)
            btn.setFixedSize(60,60)
            btn.setStyleSheet("font-size: 18px;")
            btn.clicked.connect(self.button_clicked)
            grid.addWidget(btn, row, col)

    def button_clicked(self):
        button = self.sender()
        text = button.text()

        # Clear
        if text == "C":
            self.first_number = ""
            self.operator = ""
            self.second_number = ""
            self.display.clear()
            return

        # If digit or dot
        if text.isdigit() or (text == "." and "." not in (self.first_number if self.operator == "" else self.second_number)):
            if self.operator == "":
                self.first_number += text
                self.display.setText(self.first_number)
            else:
                self.second_number += text
                self.display.setText(self.second_number)
        
        # Square
        elif text == "x^2":
            if self.first_number != "":
                num = float(self.first_number)
                result = num * num
                self.display.setText(str(result))
                self.first_number = str(result)

        # If operator
        elif text in ["+", "-", "*", "/", "x^_"]:
            if self.first_number != "":
                self.operator = text
        
        # If Equals
        elif text == "=":
            if self.first_number != "" and self.second_number != "":
                num1 = float(self.first_number)
                num2 = float(self.second_number)

                if self.operator == "+":
                    result = num1 + num2
                elif self.operator == "-":
                    result = num1 - num2
                elif self.operator == "*":
                    result = num1 * num2
                elif self.operator == "/":
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        result = "Not Divisible By Zero"
                elif self.operator == "x^_":
                    if "." in self.second_number:
                        self.display.setText("Exponent must be integer")
                        self.second_number = ""
                        return
                    
                    exponent = int(num2)

                    if exponent < 0:
                        result = 1 / (num1 ** abs(exponent))
                    else:
                        result = 1    
                        for _ in range(exponent):
                            result *= num1
                else:
                    result = "Invalid Input"
                
                self.display.setText(str(result))

                # Reset values for next calculation
                self.first_number = str(result)
                self.operator = ""
                self.second_number = ""
    
    def update_resource_usage(self):
        process = psutil.Process(os.getpid())

        # CPU Usage
        cpu = process.cpu_percent(interval=None)

        # Memory Usage(MB)
        memory = process.memory_info().rss / (1024*1024)

        self.status.showMessage(f"CPU: {cpu:.1f}% | RAM: {memory:.1f} MB")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

