from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QLineEdit, QPushButton
from app.agent.core import MikaAgent
from app.config import MIKA_NAME

class MikaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.agent = MikaAgent()
        self.setWindowTitle(f"{MIKA_NAME} Desktop AI")
        self.resize(460, 620)

        layout = QVBoxLayout(self)
        title = QLabel(MIKA_NAME)
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 28px; font-weight: 700; padding: 16px;")
        self.chat = QTextEdit()
        self.chat.setReadOnly(True)
        self.input = QLineEdit()
        self.input.setPlaceholderText("Escribe una instrucción para Mika…")
        send = QPushButton("Enviar")

        layout.addWidget(title)
        layout.addWidget(self.chat)
        layout.addWidget(self.input)
        layout.addWidget(send)

        send.clicked.connect(self.send_message)
        self.input.returnPressed.connect(self.send_message)
        self.chat.append(f"{MIKA_NAME}: Lista. ¿Qué necesitas?")

    def send_message(self):
        message = self.input.text().strip()
        if not message:
            return
        self.input.clear()
        self.chat.append(f"Tú: {message}")
        try:
            answer = self.agent.reply(message)
        except Exception as exc:
            answer = f"Error: {exc}"
        self.chat.append(f"{MIKA_NAME}: {answer}")
