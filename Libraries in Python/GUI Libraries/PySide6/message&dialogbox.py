

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget, QVBoxLayout
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        button = QPushButton("Show Message")
        button.clicked.connect(lambda: QMessageBox.information(self, 'Info', 'Hello World'))
        layout.addWidget(button)

        button1 = QPushButton("Show Message 1")
        button1.clicked.connect(self.ask_yes_no)
        layout.addWidget(button1)

        button2 = QPushButton("Show Message 2")
        button2.clicked.connect(self.ask_choice)
        layout.addWidget(button2)
        
    def ask_yes_no(self):
        if QMessageBox.question(self, 'Question', 'Do you like Python?') == QMessageBox.Yes:
            print('User likes Python')
        else:
            print('User does not like Python.')
    
    def ask_choice(self):
        msg = QMessageBox(self)

        msg.setWindowTitle('Choice')
        msg.setText('Select your favorite programming language')

        Python = msg.addButton('Python', QMessageBox.AcceptRole)
        Cpp = msg.addButton('C++', QMessageBox.AcceptRole)
        Java = msg.addButton('Java', QMessageBox.AcceptRole)

        msg.exec()

        if msg.clickedButton() == Python:
            print("User's favorite programming language is Python")
        elif msg.clickedButton() == Cpp:
            print("User's favorite programming language is C++")
        else:
            print("User's favorite programming language is Java")

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()