# In this we will learn to how to add funtionalities to some widgets


from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QTextEdit, QSlider, QProgressBar, QComboBox, QListWidget, QRadioButton, QCheckBox
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World Application")

        container = QWidget()
        self.setCentralWidget(container)

        layout_vertical = QVBoxLayout(container)

        # Label
        label1 = QLabel("Hello World")
        label1.setAlignment(Qt.AlignCenter) # To Align the label to center

        # Button
        button1 = QPushButton('Click Me') # Creating a Button
        button1.clicked.connect(lambda: print("Button Clicked")) # Adding functionalities to button

        button2 = QPushButton('Click Me Again') 
        button2.clicked.connect(self.do_something)

        # List Widget
        listwidget = QListWidget()
        listwidget.addItems(['Monday', 'Tuesday', 'Wednesday'])

        listwidget.itemClicked.connect(lambda item: print(f"Item clicked {item.text()}"))
        listwidget.itemDoubleClicked.connect(lambda item: print(f"Item doubled clicked {item.text()}"))

        # RadioButton
        inner_container2 = QWidget()
        inner_layout2 = QHBoxLayout(inner_container2)
        radio1 = QRadioButton('Thursday')
        radio2 = QRadioButton('Friday')
        radio3 = QRadioButton('Saturday')
        inner_layout2.addWidget(radio1)
        inner_layout2.addWidget(radio2)
        inner_layout2.addWidget(radio3)

        for r in (radio1,radio2,radio3):
            r.toggled.connect(self.radio_changed)


        # Calling the created widgets on the screen
        layout_vertical.addWidget(label1)
        layout_vertical.addWidget(button1)
        layout_vertical.addWidget(button2)
        layout_vertical.addWidget(listwidget)
        layout_vertical.addWidget(inner_container2)
        
    def do_something(self):
        print("Second Button Clicked")

    def radio_changed(self):
        r = self.sender()
        if r.isChecked():
            print("Radio button was selected Value:", r.text())






app = QApplication()

window = MainWindow()
window.show()

app.exec()