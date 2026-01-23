from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu Bar and Other Things")

        # Menu Bar
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('File')
        editMenu = menubar.addMenu('Edit')
        helpMenu = menubar.addMenu('?')

        aboutAction = helpMenu.addAction('About')
        
        submenu = fileMenu.addMenu('Submenu')
        exitAction = submenu.addAction('Exit')


        central_widget = QWidget()
        self.setCentralWidget(central_widget)


        layout = QVBoxLayout(central_widget)
        button = QPushButton('Show Message')
        
        layout.addWidget(button, alignment=Qt.AlignCenter)
       
        button.clicked.connect(lambda: QMessageBox.information(self, 'Info', 'Hello World'))

        exitAction.triggered.connect(self.close)
        aboutAction.triggered.connect(lambda: print('This is a tutorial GUI App'))


app = QApplication()
window = MainWindow()
window.show()
app.exec()
