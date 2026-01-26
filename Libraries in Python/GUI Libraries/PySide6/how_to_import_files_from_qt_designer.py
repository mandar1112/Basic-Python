import sys
from PySide6.QtWidgets import QApplication, QMessageBox, QLineEdit, QPushButton
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

app = QApplication(sys.argv)

loader = QUiLoader()
file = QFile(r"D:\Coding\Python\Basic\Libraries in Python\GUI Libraries\PySide6\ui files\untitled.ui")

if not file.open(QFile.ReadOnly):
    QMessageBox.critical(None, "Error", "Cannot open UI file")
    sys.exit(-1)

window = loader.load(file)
file.close()

if not window:
    QMessageBox.critical(None, "Error", "Failed to load UI")
    sys.exit(-1)

# ✅ FIND widgets by ACTUAL objectName
line_edit = window.findChild(QLineEdit, "lineEdit")   # change if needed
button = window.findChild(QPushButton, "pushButton")

if not line_edit or not button:
    QMessageBox.critical(None, "Error", "Widget not found — check objectName")
    sys.exit(-1)

button.clicked.connect(
    lambda: QMessageBox.information(window, "Message", line_edit.text())
)

window.show()
sys.exit(app.exec())
