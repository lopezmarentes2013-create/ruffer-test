import sys
from PyQt5 import QtWidgets, QtCore
from final_win import FinalWin


class SecondWin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test de Rufier - Medición")
        self.setFixedSize(400, 350)

        self.p1 = 0
        self.p2 = 0
        self.p3 = 0
        self.stage = 0

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.seconds_left = 0

        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout()

        self.instruction_label = QtWidgets.QLabel(
            "Presiona 'Comenzar' para medir tu pulso en reposo (P1) durante 15 segundos."
        )
        self.instruction_label.setWordWrap(True)
        self.instruction_label.setAlignment(QtCore.Qt.AlignCenter)

        self.timer_label = QtWidgets.QLabel("")
        self.timer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.timer_label.setStyleSheet("font-size: 30px; font-weight: bold;")

        self.pulse_input = QtWidgets.QLineEdit()
        self.pulse_input.setPlaceholderText("Ingresa el número de pulsaciones")
        self.pulse_input.setEnabled(False)

        self.action_button = QtWidgets.QPushButton("Comenzar")
        self.action_button.clicked.connect(self.handle_action)

        layout.addWidget(self.instruction_label)
        layout.addWidget(self.timer_label)
        layout.addWidget(self.pulse_input)
        layout.addWidget(self.action_button)
        self.setLayout(layout)

    def handle_action(self):
        if self.stage == 0:
            self.start_countdown(15)
            self.action_button.setEnabled(False)
        elif self.stage == 1:
            value = self.get_pulse_value()
            if value is None:
                return
            self.p1 = value
            self.pulse_input.clear()
            self.pulse_input.setEnabled(False)
            self.instruction_label.setText(
                "Ahora realiza 30 sentadillas en 45 segundos. ¡Comienza cuando estés listo!"
            )
            self.action_button.setText("Comenzar ejercicio")
            self.stage = 2
        elif self.stage == 2:
            self.instruction_label.setText("Realizando ejercicio...")
            self.start_countdown(45)
            self.action_button.setEnabled(False)
        elif self.stage == 3:
            self.instruction_label.setText(
                "Mide tu pulso durante los primeros 15 segundos después del ejercicio (P2)."
            )
            self.start_countdown(15)
            self.action_button.setEnabled(False)
        elif self.stage == 4:
            value = self.get_pulse_value()
            if value is None:
                return
            self.p2 = value
            self.pulse_input.clear()
            self.pulse_input.setEnabled(False)
            self.instruction_label.setText("Descansa 30 segundos.")
            self.start_countdown(30)
            self.action_button.setEnabled(False)
        elif self.stage == 5:
            self.instruction_label.setText(
                "Mide tu pulso durante los últimos 15 segundos del primer minuto después del ejercicio (P3)."
            )
            self.start_countdown(15)
            self.action_button.setEnabled(False)
        elif self.stage == 6:
            value = self.get_pulse_value()
            if value is None:
                return
            self.p3 = value
            self.open_final_win()
    def get_pulse_value(self):
        text = self.pulse_input.text()
        if text.isdigit():
            return int(text)
        QtWidgets.QMessageBox.warning(
            self,
            "Dato inválido",
            "Por favor ingresa solo números en el campo de pulsaciones."
        )
        return None

    def start_countdown(self, seconds):
        self.seconds_left = seconds
        self.timer_label.setText(str(self.seconds_left))
        self.timer.start(1000)

    def update_timer(self):
        self.seconds_left -= 1
        self.timer_label.setText(str(self.seconds_left))
        if self.seconds_left <= 0:
            self.timer.stop()
            self.timer_label.setText("")
            self.on_countdown_finished()

    def on_countdown_finished(self):
        if self.stage == 0:
            self.instruction_label.setText("Ingresa cuántas pulsaciones contaste (P1).")
            self.pulse_input.setEnabled(True)
            self.action_button.setText("Continuar")
            self.action_button.setEnabled(True)
            self.stage = 1
        elif self.stage == 2:
            self.instruction_label.setText("¡Ejercicio terminado!")
            self.action_button.setText("Medir P2")
            self.action_button.setEnabled(True)
            self.stage = 3
        elif self.stage == 3:
            self.instruction_label.setText("Ingresa cuántas pulsaciones contaste (P2).")
            self.pulse_input.setEnabled(True)
            self.action_button.setText("Continuar")
            self.action_button.setEnabled(True)
            self.stage = 4
        elif self.stage == 4:
            self.instruction_label.setText("Descanso terminado.")
            self.action_button.setText("Medir P3")
            self.action_button.setEnabled(True)
            self.stage = 5
        elif self.stage == 5:
            self.instruction_label.setText("Ingresa cuántas pulsaciones contaste (P3).")
            self.pulse_input.setEnabled(True)
            self.action_button.setText("Ver resultados")
            self.action_button.setEnabled(True)
            self.stage = 6

    def open_final_win(self):
        self.final_win = FinalWin(self.p1, self.p2, self.p3)
        self.final_win.show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SecondWin()
    window.show()
    sys.exit(app.exec_())