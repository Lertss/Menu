# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dodawanie_dodatkow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_new_Dodatek(object):
    def setupUi(self, new_Dodatek):
        if not new_Dodatek.objectName():
            new_Dodatek.setObjectName(u"new_Dodatek")
        new_Dodatek.resize(668, 624)
        new_Dodatek.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,\n"
"  stop:0 rgba(105, 105, 105, 255), /* \u0421\u0432\u0456\u0442\u043b\u043e-\u0441\u0456\u0440\u0438\u0439 */\n"
"  stop:0.427447 rgba(105, 105, 105, 235), /* \u0421\u0456\u0440\u0438\u0439 */\n"
"  stop:1 rgba(84, 84, 84, 255) /* \u0422\u0435\u043c\u043d\u043e-\u0441\u0456\u0440\u0438\u0439 */\n"
");\n"
"")
        self.frame = QFrame(new_Dodatek)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 10, 611, 571))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.le_title = QLabel(self.frame)
        self.le_title.setObjectName(u"le_title")
        self.le_title.setMaximumSize(QSize(16777215, 70))
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.le_title.setFont(font)
        self.le_title.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 17pt;\n"
"background-color: none;\n"
"border: none;\n"
"")
        self.le_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.le_title)

        self.le_title_4 = QLabel(self.frame)
        self.le_title_4.setObjectName(u"le_title_4")
        self.le_title_4.setMaximumSize(QSize(16777215, 70))
        self.le_title_4.setFont(font)
        self.le_title_4.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 17pt;\n"
"background-color: none;\n"
"border: none;\n"
"")
        self.le_title_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.le_title_4)

        self.dodatki = QTextEdit(self.frame)
        self.dodatki.setObjectName(u"dodatki")
        self.dodatki.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.dodatki)

        self.le_title_2 = QLabel(self.frame)
        self.le_title_2.setObjectName(u"le_title_2")
        self.le_title_2.setMaximumSize(QSize(16777215, 70))
        self.le_title_2.setFont(font)
        self.le_title_2.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 17pt;\n"
"background-color: none;\n"
"border: none;\n"
"")
        self.le_title_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.le_title_2)

        self.textEdit_eng = QTextEdit(self.frame)
        self.textEdit_eng.setObjectName(u"textEdit_eng")
        self.textEdit_eng.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.textEdit_eng)

        self.button_save_dodatek = QPushButton(self.frame)
        self.button_save_dodatek.setObjectName(u"button_save_dodatek")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(False)
        self.button_save_dodatek.setFont(font1)
        self.button_save_dodatek.setStyleSheet(u"QPushButton{\n"
"	 color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"	 width: 230;\n"
"	 height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"	 background-color:rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed{\n"
"	 background-color:rgba(255,255,255,70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/post_add_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_save_dodatek.setIcon(icon)
        self.button_save_dodatek.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.button_save_dodatek)


        self.retranslateUi(new_Dodatek)

        QMetaObject.connectSlotsByName(new_Dodatek)
    # setupUi

    def retranslateUi(self, new_Dodatek):
        new_Dodatek.setWindowTitle(QCoreApplication.translate("new_Dodatek", u"Dialog", None))
        self.le_title.setText(QCoreApplication.translate("new_Dodatek", u"Dodawanie dodatk\u00f3w", None))
        self.le_title_4.setText(QCoreApplication.translate("new_Dodatek", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt;\">Dodatki</span></p></body></html>", None))
        self.le_title_2.setText(QCoreApplication.translate("new_Dodatek", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt;\">Dodatki po angielsku</span></p></body></html>", None))
        self.button_save_dodatek.setText(QCoreApplication.translate("new_Dodatek", u"Doda\u0107 opisanie dodatk\u00f3w", None))
    # retranslateUi

