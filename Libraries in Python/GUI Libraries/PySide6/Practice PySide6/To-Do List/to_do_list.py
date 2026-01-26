
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QDateTime
import json, sys


class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()

       

        self.setWindowTitle("To-Do List")
        self.setGeometry(300,200, 400, 400)

        # Create Layout
        self.layout = QVBoxLayout()

        # Input & Button
        self.input_layout = QHBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter a task: ")
        self.add_button = QPushButton("Add")

        self.input_layout.addWidget(self.task_input)
        self.input_layout.addWidget(self.add_button)

        # Task List
        self.task_list = QListWidget()

        # Load Task
        self.load_tasks()

        # Delete Button
        self.delete_button = QPushButton("Delete")

        # Add Layout
        self.layout.addLayout(self.input_layout)
        self.layout.addWidget(self.task_list)
        self.layout.addWidget(self.delete_button)

        # Create Central Widget
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        # Connect Buttons
        self.add_button.clicked.connect(self.add_task)
        self.task_list.itemDoubleClicked.connect(self.toggle_task_status)
        self.delete_button.clicked.connect(self.delete_task)


    def add_task(self):
        self.task_text = self.task_input.text().strip()
        if not self.task_text:
            QMessageBox.warning(self, "Warning", "Task cannot be empty!")
            return
        
        timestamp = QDateTime.currentDateTime().toString("dd-MM-yyyy hh:mm AP")
        full_text = f"{self.task_text} | {timestamp}"

        item = QListWidgetItem(full_text)
        item.setCheckState(Qt.Unchecked)
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)

        self.task_list.addItem(item)
        self.task_input.clear()


    def delete_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            self.task_list.takeItem(self.task_list.row(selected_item))
        else:
            QMessageBox.warning(self, "Warning", "No Task Selected!")
    
    def save_tasks(self):
        tasks = []
        for i in range(self.task_list.count()):
            item = self.task_list.item(i)
            tasks.append({
                "text": item.text(),
                "checked": item.checkState() == Qt.Checked
            })
        
        try:
            with open("tasks.json", "wt") as fh:
                json.dump(tasks, fh)
        except Exception as e:
            QMessageBox.warning(self, "Warning", f"Error: {e}")
    
    def load_tasks(self):
        try:
            with open("tasks.json", "rt") as fh:
                tasks = json.load(fh)
            for task in tasks:
                item = QListWidgetItem(task["text"])
                item.setCheckState(Qt.Checked if task["checked"] else Qt.Unchecked)
                item.setFlags(item.flags() | Qt.ItemIsUserCheckable)

                font = item.font()
                font.setStrikeOut(task["checked"])
                item.setFont(font)
                
                self.task_list.addItem(item)
        except FileNotFoundError:
            pass

    def toggle_task_status(self, item):
        font = item.font()

        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
            font.setStrikeOut(False)
            item.setFont(font)
        else:
            item.setCheckState(Qt.Checked)
            font.setStrikeOut(True)
            item.setFont(font)

    def closeEvent(self, event):
        self.save_tasks()
        event.accept()
        # return super().closeEvent(event)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec())