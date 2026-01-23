from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QTextEdit, QSlider, QProgressBar, QComboBox, QListWidget, QRadioButton, QCheckBox
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World Application")

        container = QWidget()
        self.setCentralWidget(container)

        # There are three most important layout in PySide6

        layout_vertical = QVBoxLayout(container)
        # layout_horizontal = QHBoxLayout(container)
        # layout_grid = QGridLayout(container)

        

        """
        label2 = QLabel("One")
        label2.setAlignment(Qt.AlignCenter)
        
        label3 = QLabel("Two")
        label3.setAlignment(Qt.AlignCenter)

        label4 = QLabel("Three")
        label4.setAlignment(Qt.AlignCenter)

        label5 = QLabel("Four")
        label5.setAlignment(Qt.AlignCenter)

        
        layout_vertical.addWidget(label1)
        layout_vertical.addWidget(label2)
        layout_vertical.addWidget(label3)
        layout_vertical.addWidget(label4)
        layout_vertical.addWidget(label5)
        
        layout_horizontal.addWidget(label1)
        layout_horizontal.addWidget(label2)
        layout_horizontal.addWidget(label3)
        layout_horizontal.addWidget(label4)
        layout_horizontal.addWidget(label5)
        
        layout_grid.addWidget(label1, 0, 0)
        layout_grid.addWidget(label2, 0, 1)
        layout_grid.addWidget(label3, 1, 0)
        layout_grid.addWidget(label4, 1, 1)
        layout_grid.addWidget(label5, 2, 1)
        """

        # Label
        label1 = QLabel("Hello World")
        label1.setAlignment(Qt.AlignCenter) # To Align the label to center

        # Button
        button = QPushButton('Click Me') # Creating a Button

        # Text
        line_edit = QLineEdit() # Creating a single line to write text just like entry
        text_edit = QTextEdit() # Creating a mulit line to write text just like text box

        # ComboBox
        combobox = QComboBox()
        combobox.addItems(['One', 'Two', 'Three'])

        # List Widget
        listwidget = QListWidget()
        listwidget.addItems(['One', 'Two', 'Three'])

        
        # CheckBox
        inner_container1 = QWidget()
        inner_layout1 = QHBoxLayout(inner_container1)

        checkbox1 = QCheckBox('Monday')
        checkbox2 = QCheckBox('Tuesday')
        checkbox3 = QCheckBox('Wednesday')
        inner_layout1.addWidget(checkbox1)
        inner_layout1.addWidget(checkbox2)
        inner_layout1.addWidget(checkbox3)

        # RadioButton
        inner_container2 = QWidget()
        inner_layout2 = QHBoxLayout(inner_container2)
        radio1 = QRadioButton('Thursday')
        radio2 = QRadioButton('Friday')
        radio3 = QRadioButton('Saturday')
        inner_layout2.addWidget(radio1)
        inner_layout2.addWidget(radio2)
        inner_layout2.addWidget(radio3)

        # Slider

        slider = QSlider(Qt.Horizontal)
        slider.setRange(0,100)

        # ProgressBar

        progressbar = QProgressBar()

        # Calling the created widgets on the screen
        layout_vertical.addWidget(label1)
        layout_vertical.addWidget(button)
        layout_vertical.addWidget(line_edit)
        layout_vertical.addWidget(text_edit)
        layout_vertical.addWidget(combobox)
        layout_vertical.addWidget(listwidget)
        layout_vertical.addWidget(inner_container1)
        layout_vertical.addWidget(inner_container2)
        layout_vertical.addWidget(slider)
        layout_vertical.addWidget(progressbar)
        
        





app = QApplication()

window = MainWindow()
window.show()

app.exec()