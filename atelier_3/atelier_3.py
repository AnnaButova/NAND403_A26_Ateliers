from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QTextEdit, QMessageBox
 
class MessageBoard(QWidget):
    def __init__(self): # Constructeur
        super().__init__() # Constructeur QWidget
        self.setWindowTitle("Message board")
        self.create_ui()
    
    def create_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Message Board")
        layout.addWidget(label)

        text_edit = QTextEdit(self)
        layout.addWidget(text_edit)
        text_bar = QMessageBox(text_edit)

 
        # QTextEdit
        # QPushButton
    
   
    def on_click(self):
        print("on click called")
        # QMessageBox
   
 
def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()
 
main()