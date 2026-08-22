import sys
from PyQt5 import QtWidgets, QtCore


class FinalWin(QtWidgets.QWidget):
    def __init__(self, p1, p2, p3):
        super().__init__()
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        self.setWindowTitle("Resultado del Test de Rufier")
        self.setFixedSize(400, 300)

        self.index = self.calculate_index()
        self.init_ui()

    def calculate_index(self):
        return round((4 * (self.p1 + self.p2 + self.p3) - 200) / 10, 1)


    def get_evaluation(self):
        if self.index < 0:
            return "Excelente"
        elif self.index <= 5:
            return "Buena"
        elif self.index <= 10:
            return "Media"
        elif self.index <= 15:
            return "Satisfactoria"
        else:
            return "Mala"

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout()

        title = QtWidgets.QLabel("Resultados")
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")

        details = QtWidgets.QLabel(f"P1: {self.p1}    P2: {self.p2}    P3: {self.p3}")
        details.setAlignment(QtCore.Qt.AlignCenter)

        index_label = QtWidgets.QLabel(f"Índice de Rufier: {self.index}")
        index_label.setAlignment(QtCore.Qt.AlignCenter)
        index_label.setStyleSheet("font-size: 18px;")

        evaluation_label = QtWidgets.QLabel(f"Evaluación: {self.get_evaluation()}")
        evaluation_label.setAlignment(QtCore.Qt.AlignCenter)
        evaluation_label.setStyleSheet("font-size: 18px; font-weight: bold;")

        close_button = QtWidgets.QPushButton("Cerrar")
        close_button.clicked.connect(self.close)

        layout.addWidget(title)
        layout.addWidget(details)
        layout.addWidget(index_label)
        layout.addWidget(evaluation_label)
        layout.addWidget(close_button)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FinalWin(70, 90, 80)
    window.show()
    sys.exit(app.exec_())