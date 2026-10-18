import random
from maya import cmds
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QSpinBox,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QFormLayout
)

class RandomGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 4-5")
        self.setMinimumWidth(400)
        self.build_ui()
    
    def build_ui(self):
        table_layout = QFormLayout(self) # form layout
        

        # Create box for number of objects
        row1 = QHBoxLayout()
        row1.addWidget(QLineEdit(""))
        table_layout.addRow(QLabel("Number of Objects"), row1)

        # Create min and max indicators
        rowX = QHBoxLayout()
        rowX.addWidget(QLabel("Min                                        "))
        rowX.addWidget(QLabel("Max"))
        table_layout.addRow(QLabel(""), rowX)

        # Create box for Position X
        row2 = QHBoxLayout()
        row2.addWidget(QLineEdit(""))
        row2.addWidget(QLineEdit(""))
        table_layout.addRow(QLabel("Position X"), row2)

        # Create box for Position Y
        row3 = QHBoxLayout()
        row3.addWidget(QLineEdit(""))
        row3.addWidget(QLineEdit(""))
        table_layout.addRow(QLabel("Position Y"), row3)

        # Create box for Position Z
        row4 = QHBoxLayout()
        row4.addWidget(QLineEdit(""))
        row4.addWidget(QLineEdit(""))
        table_layout.addRow(QLabel("Position Z"), row4)
     
        # Create box for Scale
        row5 = QHBoxLayout()
        row5.addWidget(QLineEdit(""))
        row5.addWidget(QLineEdit(""))
        table_layout.addRow(QLabel("Scale"), row5)

        # Create Button
        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_object)
        table_layout.addRow(self.create_button)
        
        

    def create_object(self):
        forme = random.choice(["cube", "cylindre", "sphere"])

        if forme == "cube":
            objet = cmds.polyCube()[0]
        elif forme == "cylindre":
            objet = cmds.polyCylinder()[0]
        else:
            objet = cmds.polySphere()[0]

        random_value = random.uniform(-10, 10)
        cmds.move(random_value, random_value, random_value, objet)


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomGenerator()
    tool_window.show()

main()