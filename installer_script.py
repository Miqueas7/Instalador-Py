import os
import shutil
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QMessageBox

class InstallerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Shift Gamma Installer')
        self.setGeometry(100, 100, 300, 150)

        # Layout principal
        layout = QVBoxLayout()

        # Mensaje de bienvenida
        self.label = QLabel("Bienvenido al instalador de Shift Gamma", self)
        layout.addWidget(self.label)

        # Botón de instalación
        self.install_button = QPushButton('Instalar', self)
        self.install_button.clicked.connect(self.install_files)
        layout.addWidget(self.install_button)

        # Widget principal
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def install_files(self):
        try:
            user_home = str(Path.home())
            excel_target_path = os.path.join(user_home, "AppData", "Roaming", "Microsoft", "AddIns")
            access_target_path = os.path.join(user_home, "Documentos", "Shift Gamma")

            # Archivos a copiar (debes incluir estos archivos en el directorio del instalador)
            source_excel = "resources/libro1.xlam"
            source_access = "resources/DB.accdb"

            # Crear directorios si no existen
            os.makedirs(excel_target_path, exist_ok=True)
            os.makedirs(access_target_path, exist_ok=True)

            # Copiar archivos
            shutil.copy2(source_excel, excel_target_path)
            shutil.copy2(source_access, access_target_path)

            QMessageBox.information(self, "Instalación Completada", "Los archivos se han instalado correctamente.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error durante la instalación: {str(e)}")

if __name__ == '__main__':
    app = QApplication([])
    installer = InstallerApp()
    installer.show()
    app.exec()
