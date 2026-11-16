from PySide6.QtWidgets import QWidget, QSlider, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt
from maya import cmds
import maya.OpenMayaUI as omui
from shiboken6 import wrapInstance

# always show ui on top of maya window
def maya_main_window():
    pointer = omui.MQtUtil.mainWindow()
    return wrapInstance(int(pointer), QWidget)


class LiveScale(QWidget):
    def __init__(self):
        super().__init__(maya_main_window())
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle("Live Scale")
        self.build_ui()

    def build_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.scale_slider = QSlider()
        self.scale_slider.setOrientation(Qt.Horizontal)
        self.main_layout.addWidget(self.scale_slider)
        self.apply_button = QPushButton("Apply Scale")
        self.apply_button.clicked.connect(self.on_apply_scale_clicked)
        self.main_layout.addWidget(self.apply_button)

    def on_apply_scale_clicked(self):
        scale_factor = self.scale_slider.value()/10.0
        selection = cmds.ls(selection=True, transforms=True)
        for obj in selection:
            cmds.setAttr(f"{obj}.scale", scale_factor, scale_factor, scale_factor)
            
def show_live_scale():
    global live_scale
    try:
        live_scale.close()
    except:
        pass
    live_scale = LiveScale()
    live_scale.show()

show_live_scale()
