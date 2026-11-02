from PySide6.QtWidgets import(
    QWidget
)

class MyClass(QWidget):
    def __init__(self):
        self.variable = 42
        
    def print_variable(self):
        print(self.variable)