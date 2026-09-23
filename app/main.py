import sys
from PySide6.QtWidgets import QApplication
from app.ui.window import MikaWindow

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Mika Desktop AI")
    window = MikaWindow()
    window.show()
    return app.exec()

if __name__ == "__main__":
    raise SystemExit(main())
