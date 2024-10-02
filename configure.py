import sys

from PySide6.QtCore import Slot, QSettings
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QComboBox
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo

from PySide6.QtWidgets import QDialog

from ui_configure import Ui_Configure

BLANK_STRING = "N/A"

CUSTOM_BAUDRATE_INDEX = 4

class Settings():

    def __init__(self):
        self.name = ""
        self.baud_rate = 0
        self.string_baud_rate = ""
        self.data_bits = QSerialPort.Data8
        self.string_data_bits = ""
        self.parity = QSerialPort.NoParity
        self.string_parity = ""
        self.stop_bits = QSerialPort.OneStop
        self.string_stop_bits = ""
        self.flow_control = QSerialPort.SoftwareControl
        self.string_flow_control = ""

class Configure(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.m_ui = Ui_Configure()
        self._custom_port_index = -1
        self.m_ui.setupUi(self)
        self.m_currentSettings = Settings()
        self.m_settings = QSettings("STM32Uploader")
        self.m_intValidator = QIntValidator(0, 4000000, self)

        self.m_ui.baudRateBox.setInsertPolicy(QComboBox.NoInsert)

        self.m_ui.Apply_Button.clicked.connect(self.apply)
        self.m_ui.serialPortInfoListBox.currentIndexChanged.connect(self.show_port_info)
        self.m_ui.baudRateBox.currentIndexChanged.connect(self.check_custom_baud_rate_policy)
        self.m_ui.serialPortInfoListBox.currentIndexChanged.connect(
            self.check_custom_device_path_policy)

        self.fill_ports_parameters()
        self.fill_ports_info()

        self.update_settings()

    def settings(self):
        return self.m_currentSettings
