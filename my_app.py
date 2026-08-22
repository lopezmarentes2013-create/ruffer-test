import sys
from PyQt5 import QtWidgets, QtCore
from instrucciones import InstrWin


class MainWin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test de Rufier")
        self.setFixedSize(400, 300)
        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout()

        title = QtWidgets.QLabel("Bienvenido al Test de Rufier")
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold;")

        desc = QtWidgets.QLabel("Esta aplicación te ayudará a evaluar\ntu condición cardiovascular.")
        desc.setAlignment(QtCore.Qt.AlignCenter)

        self.start_button = QtWidgets.QPushButton("Iniciar")
        self.start_button.clicked.connect(self.open_instructions)

        layout.addWidget(title)
        layout.addWidget(desc)
        layout.addWidget(self.start_button)
        self.setLayout(layout)

    def open_instructions(self):
        self.instr_win = InstrWin()
        self.instr_win.show()
        self.close()