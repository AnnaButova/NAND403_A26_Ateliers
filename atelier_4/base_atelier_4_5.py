import random
from maya import cmds
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QSpinBox,
    QDoubleSpinBox,
    QLabel
)

class RandomGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 4-5")
        self.setMinimumWidth(400)
        self.build_ui()
    
    def build_ui(self):
        layout_V = QVBoxLayout(self) # vertical layout

       
        # Create box for number of objects
        row1 = QHBoxLayout()
        row1.addWidget(QLabel("Number of Objects"))
        self.nb_objects_field = QSpinBox()
        row1.addWidget(self.nb_objects_field)
        layout_V.addLayout(row1)

        # Create box for Position X
        row2 = QHBoxLayout()
        row2.addWidget(QLabel("Position X"))
        self.position_x_field_min = QDoubleSpinBox()
        self.position_x_field_max = QDoubleSpinBox()
        row2.addWidget(self.position_x_field_min)
        row2.addWidget(self.position_x_field_max)
        layout_V.addLayout(row2)

        # Create box for Position Y
        row3 = QHBoxLayout()
        row3.addWidget(QLabel("Position Y"))
        self.position_y_field_min = QDoubleSpinBox()
        self.position_y_field_max = QDoubleSpinBox()
        row3.addWidget(self.position_y_field_min)
        row3.addWidget(self.position_y_field_max)
        layout_V.addLayout(row3)

        # Create box for Position Z
        row4 = QHBoxLayout()
        row4.addWidget(QLabel("Position Z"))
        self.position_z_field_min = QDoubleSpinBox()
        self.position_z_field_max = QDoubleSpinBox()
        row4.addWidget(self.position_z_field_min)
        row4.addWidget(self.position_z_field_max)
        layout_V.addLayout(row4)
        layout_V.addLayout(row2)

        # Create box for Scale
        row5 = QHBoxLayout()
        row5.addWidget(QLabel("Scale"))
        self.scale_field_min = QDoubleSpinBox()
        self.scale_field_max = QDoubleSpinBox()
        row5.addWidget(self.scale_field_min)
        row5.addWidget(self.scale_field_max)
        layout_V.addLayout(row5)

        # Create Button
        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_object)
        layout_V.addWidget(self.create_button)
        

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