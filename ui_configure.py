# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configure.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QToolButton, QWidget)

class Ui_Configure(object):
    def setupUi(self, Configure):
        if not Configure.objectName():
            Configure.setObjectName(u"Configure")
        Configure.resize(349, 319)
        self.BaudRateLabel = QLabel(Configure)
        self.BaudRateLabel.setObjectName(u"BaudRateLabel")
        self.BaudRateLabel.setGeometry(QRect(170, 20, 81, 20))
        self.BaudRateBox = QComboBox(Configure)
        self.BaudRateBox.setObjectName(u"BaudRateBox")
        self.BaudRateBox.setGeometry(QRect(250, 20, 71, 21))
        self.DatabitsBox = QComboBox(Configure)
        self.DatabitsBox.setObjectName(u"DatabitsBox")
        self.DatabitsBox.setGeometry(QRect(250, 60, 71, 21))
        self.DatabitsLabel = QLabel(Configure)
        self.DatabitsLabel.setObjectName(u"DatabitsLabel")
        self.DatabitsLabel.setGeometry(QRect(170, 60, 81, 20))
        self.Ok_Button = QPushButton(Configure)
        self.Ok_Button.setObjectName(u"Ok_Button")
        self.Ok_Button.setGeometry(QRect(100, 280, 75, 24))
        self.Cancel_Button = QPushButton(Configure)
        self.Cancel_Button.setObjectName(u"Cancel_Button")
        self.Cancel_Button.setGeometry(QRect(180, 280, 75, 24))
        self.Apply_Button = QPushButton(Configure)
        self.Apply_Button.setObjectName(u"Apply_Button")
        self.Apply_Button.setGeometry(QRect(260, 280, 75, 24))
        self.ParityLabel = QLabel(Configure)
        self.ParityLabel.setObjectName(u"ParityLabel")
        self.ParityLabel.setGeometry(QRect(170, 100, 81, 20))
        self.ParityBox = QComboBox(Configure)
        self.ParityBox.setObjectName(u"ParityBox")
        self.ParityBox.setGeometry(QRect(250, 100, 71, 21))
        self.StopbitsLabel = QLabel(Configure)
        self.StopbitsLabel.setObjectName(u"StopbitsLabel")
        self.StopbitsLabel.setGeometry(QRect(170, 140, 81, 20))
        self.StopbitsBox = QComboBox(Configure)
        self.StopbitsBox.setObjectName(u"StopbitsBox")
        self.StopbitsBox.setGeometry(QRect(250, 140, 71, 21))
        self.FlowcontrolLabel = QLabel(Configure)
        self.FlowcontrolLabel.setObjectName(u"FlowcontrolLabel")
        self.FlowcontrolLabel.setGeometry(QRect(170, 180, 81, 20))
        self.FlowcontrolBox = QComboBox(Configure)
        self.FlowcontrolBox.setObjectName(u"FlowcontrolBox")
        self.FlowcontrolBox.setGeometry(QRect(250, 180, 71, 21))
        self.SelectLabel = QLabel(Configure)
        self.SelectLabel.setObjectName(u"SelectLabel")
        self.SelectLabel.setGeometry(QRect(20, 20, 101, 21))
        self.SelectBox = QComboBox(Configure)
        self.SelectBox.setObjectName(u"SelectBox")
        self.SelectBox.setGeometry(QRect(20, 50, 91, 21))
        self.descriptionLabel = QLabel(Configure)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        self.descriptionLabel.setGeometry(QRect(20, 90, 86, 16))
        self.CLI_Label = QLabel(Configure)
        self.CLI_Label.setObjectName(u"CLI_Label")
        self.CLI_Label.setGeometry(QRect(10, 230, 201, 21))
        self.CLI_pathButton = QToolButton(Configure)
        self.CLI_pathButton.setObjectName(u"CLI_pathButton")
        self.CLI_pathButton.setGeometry(QRect(200, 230, 22, 22))

        self.retranslateUi(Configure)

        QMetaObject.connectSlotsByName(Configure)
    # setupUi

    def retranslateUi(self, Configure):
        Configure.setWindowTitle(QCoreApplication.translate("Configure", u"Dialog", None))
        self.BaudRateLabel.setText(QCoreApplication.translate("Configure", u"BaudRate:", None))
        self.DatabitsLabel.setText(QCoreApplication.translate("Configure", u"Data bits:", None))
        self.Ok_Button.setText(QCoreApplication.translate("Configure", u"OK", None))
        self.Cancel_Button.setText(QCoreApplication.translate("Configure", u"Cancel", None))
        self.Apply_Button.setText(QCoreApplication.translate("Configure", u"Apply", None))
        self.ParityLabel.setText(QCoreApplication.translate("Configure", u"Parity:", None))
        self.StopbitsLabel.setText(QCoreApplication.translate("Configure", u"Stop bits:", None))
        self.FlowcontrolLabel.setText(QCoreApplication.translate("Configure", u"Flow control:", None))
        self.SelectLabel.setText(QCoreApplication.translate("Configure", u"Select Serial Port", None))
        self.descriptionLabel.setText(QCoreApplication.translate("Configure", u"Description:", None))
        self.CLI_Label.setText(QCoreApplication.translate("Configure", u"STM32_Programmer_CLI.exe path:", None))
        self.CLI_pathButton.setText(QCoreApplication.translate("Configure", u"...", None))
    # retranslateUi

