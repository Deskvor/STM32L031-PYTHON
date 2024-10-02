# This Python file uses the following encoding: utf-8
import sys
import subprocess

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import QSettings
from ui_mainwindow import Ui_MainWindow
from configure import Configure


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.m_settings = QSettings("STM32Uploader")

        self.ui.Browse_pushButton.clicked.connect(self.browse_file)
        self.ui.Start_pushButton.clicked.connect(self.upload_hex)
        self.selected_hex_file = None

    def browse_file(self):
                file_dialog = QFileDialog(self)
                file_path, _ = file_dialog.getOpenFileName(self, "Select .hex file", "", "Hex Files (*.hex)")

                if file_path:
                    self.selected_hex_file = file_path
                    self.ui.lineEdit.setText(file_path)

    def upload_hex(self):
            if not self.selected_hex_file:
                QMessageBox.warning(self, "Error", "Please select a .hex file before starting.")
                return

            cli_path = r"E:\Programs\STM32CUBEProgrammer\bin\STM32_Programmer_CLI.exe"

            try:
                # Command to upload the hex file using STM32CubeProgrammer CLI
                command = [
                    cli_path,
                    "-c", "port=SWD", "mode=UR",    # Port and mode parameters
                    "-w", self.selected_hex_file,   # Write the selected .hex file
                    "-v", "-rst"                    # Verify and reset after flashing
                ]

                result = subprocess.run(command, capture_output=True, text=True)

                if result.returncode == 0:
                    QMessageBox.information(self, "Success", "Hex file successfully uploaded to STM32!")
                else:
                    error_message = result.stderr if result.stderr else result.stdout
                    QMessageBox.critical(self, "Error", f"Failed to upload hex file.\nError: {error_message}")

            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
