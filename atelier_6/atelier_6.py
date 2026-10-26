from maya import cmds
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QMainWindow,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
    QDoubleSpinBox
    )

class MainWindow(QMainWindow)
    class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fence Generation")
        self.build_ui()

    def build_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout_v = QVBoxLayout(central_widget)

        self.fence_number = QDoubleSpinBox("Number of fences")
        self.spacing = QDoubleSpinBox("Spacing")

window = MainWindow()
window.show()