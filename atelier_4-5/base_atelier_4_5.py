import random
from maya import cmds
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QFormLayout
)

class RandomGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 4-5")
        self.setFixedWidth(400)
        self.setFixedHeight(210)
        self.build_ui()
    
    def build_ui(self):
        table_layout = QFormLayout(self) # form layout
        

        # Create box for number of objects
        row1 = QHBoxLayout()
        self.number_of_objects_input = QLineEdit("1")
        row1.addWidget(self.number_of_objects_input)
        table_layout.addRow(QLabel("Number of Objects"), row1)

        # Create min and max indicators
        table_layout.addRow(QLabel(""), QLabel(" Min                                       Max"))

        # Create box for Position X
        row2 = QHBoxLayout()
        self.position_x_min_input = QLineEdit("0")
        self.position_x_max_input = QLineEdit("0")
        row2.addWidget(self.position_x_min_input)
        row2.addWidget(self.position_x_max_input)
        table_layout.addRow(QLabel("Position X"), row2)

        # Create box for Position Y
        row3 = QHBoxLayout()
        self.position_y_min_input = QLineEdit("0")
        self.position_y_max_input = QLineEdit("0")
        row3.addWidget(self.position_y_min_input)
        row3.addWidget(self.position_y_max_input)
        table_layout.addRow(QLabel("Position Y"), row3)

        # Create box for Position Z
        row4 = QHBoxLayout()
        self.position_z_min_input = QLineEdit("0")
        self.position_z_max_input = QLineEdit("0")
        row4.addWidget(self.position_z_min_input)
        row4.addWidget(self.position_z_max_input)
        table_layout.addRow(QLabel("Position Z"), row4)
     
        # Create box for Scale
        row5 = QHBoxLayout()
        self.scale_min_input = QLineEdit("1")
        self.scale_max_input = QLineEdit("1")
        row5.addWidget(self.scale_min_input)
        row5.addWidget(self.scale_max_input)
        table_layout.addRow(QLabel("Scale"), row5)

        # Create Button
        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_object)
        table_layout.addRow(self.create_button)
        
        

    def create_object(self):

        number_of_objects = int(self.number_of_objects_input.text()) # user input for number of objects

        for i in range(number_of_objects):

            forme = random.choice(["cube", "cylindre", "sphere"]) # an array of forms that will spawn
            if forme == "cube":
                objet = cmds.polyCube()[0]
            elif forme == "cylindre":
                objet = cmds.polyCylinder()[0]
            else:
                objet = cmds.polySphere()[0]

            # creating variables for min and max values based on user input
            x_min = float(self.position_x_min_input.text())
            x_max = float(self.position_x_max_input.text())

            y_min = float(self.position_y_min_input.text())
            y_max = float(self.position_y_max_input.text())

            z_min = float(self.position_z_min_input.text())
            z_max = float(self.position_z_max_input.text())

            # generating random values for position and scale based on user input
            random_x = random.uniform(x_min, x_max)
            random_y = random.uniform(y_min, y_max)
            random_z = random.uniform(z_min, z_max)

            # generating random scale based on user input
            random_scale = random.uniform(float(self.scale_min_input.text()), float(self.scale_max_input.text()))

            # applying random values to the object
            cmds.scale(random_scale, random_scale, random_scale, objet)
            cmds.move(random_x, random_y, random_z, objet)


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomGenerator()
    tool_window.show()

main()