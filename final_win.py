from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from instrucciones import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.result_label = QLabel(txt_result_placeholder)
        self.performance_label = QLabel(txt_performance_placeholder)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.result_label)
        self.layout.addWidget(self.performance_label)
        self.setLayout(self.layout)