from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QTextEdit, QMessageBox, QPushButton
 
class MessageBoard(QWidget):
    def __init__(self): # Constructeur
        super().__init__() # Constructeur QWidget
        self.setWindowTitle("Message board")
        self.create_ui()
    
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

        # Button pressed logic
        def show_user_message():
            user_input = text_edit.toPlainText()
            print(user_input)
        
        if button_ok.pressed.connect(show_user_message):
            widget.show()
            
    
   
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

