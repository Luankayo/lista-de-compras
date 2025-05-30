# main.py
import sys
from PyQt6.QtWidgets import QApplication
from ui.tela_principal import TelaPrincipal

def main():
    app = QApplication(sys.argv)
    janela = TelaPrincipal()
    janela.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
