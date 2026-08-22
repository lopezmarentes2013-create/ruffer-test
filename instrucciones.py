import sys
from PyQt5 import QtWidgets, QtCore
from second_win import SecondWin


class InstrWin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Instrucciones")
        self.setFixedSize(400, 300)

        self.pages = [
            "Paso 1:\nSiéntate y relájate durante 1 minuto.",
            "Paso 2:\nMediremos tu pulso en reposo (P1).",
            "Paso 3:\nHarás 30 sentadillas en 45 segundos.",
            "Paso 4:\nMediremos tu pulso después del ejercicio (P2 y P3)."
        ]
        self.current_index = 0

        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout()

        self.text_label = QtWidgets.QLabel(self.pages[self.current_index])
        self.text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.text_label.setWordWrap(True)
        self.text_label.setStyleSheet("font-size: 16px;")

        buttons_layout = QtWidgets.QHBoxLayout()
        self.back_button = QtWidgets.QPushButton("Atrás")
        self.back_button.clicked.connect(self.back_click)
        self.next_button = QtWidgets.QPushButton("Siguiente")
        self.next_button.clicked.connect(self.next_click)

        buttons_layout.addWidget(self.back_button)
        buttons_layout.addWidget(self.next_button)

        self.start_test_button = QtWidgets.QPushButton("Comenzar prueba")
        self.start_test_button.clicked.connect(self.open_second_win)
        self.start_test_button.setEnabled(False)

        layout.addWidget(self.text_label)
        layout.addLayout(buttons_layout)
        layout.addWidget(self.start_test_button)
        self.setLayout(layout)

    def next_click(self):
        if self.current_index < len(self.pages) - 1:
            self.current_index += 1
            self.text_label.setText(self.pages[self.current_index])
        if self.current_index == len(self.pages) - 1:
            self.start_test_button.setEnabled(True)

    def back_click(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.text_label.setText(self.pages[self.current_index])
            self.start_test_button.setEnabled(False)

    def open_second_win(self):
        self.second_win = SecondWin()
        self.second_win.show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = InstrWin()
    window.show()
    sys.exit(app.exec_())