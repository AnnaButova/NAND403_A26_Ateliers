from maya import cmds
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QMainWindow,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLabel,
    QDoubleSpinBox
    )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fence Generation")
        self.build_ui()

    def build_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout_v = QVBoxLayout(central_widget)
        sub_layout_h1 = QHBoxLayout()
        sub_layout_h2 = QHBoxLayout()

        self.label_fence_nb = QLabel("Fence Number")
        self.label_spacing = QLabel("Spacing")
        self.fence_number = QDoubleSpinBox(self)
        self.spacing = QDoubleSpinBox(self)

        sub_layout_h1.addWidget(self.label_fence_nb)
        sub_layout_h1.addWidget(self.fence_number)
        sub_layout_h1.addWidget(self.label_spacing)
        sub_layout_h1.addWidget(self.spacing)

        self.label_height = QLabel("Fence Height")
        self.fence_height = QDoubleSpinBox(self)

        sub_layout_h2.addWidget(self.label_height)
        sub_layout_h2.addWidget(self.fence_height)

        self.generate_button = QPushButton("Generate!")

        layout_v.addLayout(sub_layout_h1)
        layout_v.addLayout(sub_layout_h2)
        layout_v.addWidget(self.generate_button)

    def spawn_fence(self):
        self.fence_v_length = 10
        self.fence_v_width = 2
        self.fence_v_depth = self.fence_v_width / 1.5

        self.fence_h_length = self.fence_v_length
        self.fence_h_width = self.fence_v_width
        self.fence_h_depth = self.fence_v_depth

window = MainWindow()
window.show()