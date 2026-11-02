# classic library import
import os
import sys
from PySide6.QtWidgets import(
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton
)
'''# get folder of current file
# __file__ = current file
absolute_file_path = os.path.abspath(__file__)
absolute_folder_path = os.path.dirname(absolute_file_path)
print(absolute_folder_path)

# add absolute folder path to python path, so that it can detect the library
sys.path.append(absolute_folder_path)'''

import ui

class MessageBoard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Animation Tool")
        self.setMinimumWidth(400)
        
    def create_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Message board")
        layout.addWidget(label)

        # Creating text box
        text_edit = QTextEdit(self)
        layout.addWidget(text_edit)
        text_edit.setPlaceholderText("Type your message...")

        # Creating button
        button_ok = QPushButton("PRINT")
        layout.addWidget(button_ok)
