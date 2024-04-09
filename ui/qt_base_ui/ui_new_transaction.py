# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_new_transaction.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_New_transaction(object):
    def setupUi(self, New_transaction):
        if not New_transaction.objectName():
            New_transaction.setObjectName(u"New_transaction")
        New_transaction.resize(477, 436)
        New_transaction.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,\n"
"  stop:0 rgba(128, 128, 128, 255), /* \u0421\u0432\u0456\u0442\u043b\u043e-\u0441\u0456\u0440\u0438\u0439 */\n"
"  stop:0.427447 rgba(85, 85, 85, 235), /* \u0421\u0456\u0440\u0438\u0439 */\n"
"  stop:1 rgba(64, 64, 64, 255) /* \u0422\u0435\u043c\u043d\u043e-\u0441\u0456\u0440\u0438\u0439 */\n"
");\n"
"")
        self.horizontalLayout = QHBoxLayout(New_transaction)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(New_transaction)
        self.frame.setObjectName(u"frame")
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
        self.le_title.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;\n"
"")
        self.le_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.le_title)

        self.cb_category = QComboBox(self.frame)
        self.cb_category.setObjectName(u"cb_category")
        self.cb_category.setStyleSheet(u"QComboBox {\n"
"font-size: 16pt;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"    color: black;\n"
"}")

        self.verticalLayout.addWidget(self.cb_category)

        self.le_name = QLineEdit(self.frame)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.le_name)

        self.le_description = QLineEdit(self.frame)
        self.le_description.setObjectName(u"le_description")
        self.le_description.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.le_description)

        self.le_description_eng = QLineEdit(self.frame)
        self.le_description_eng.setObjectName(u"le_description_eng")
        self.le_description_eng.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.le_description_eng)

        self.le_masa = QLineEdit(self.frame)
        self.le_masa.setObjectName(u"le_masa")
        self.le_masa.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.le_masa)

        self.le_cena = QLineEdit(self.frame)
        self.le_cena.setObjectName(u"le_cena")
        self.le_cena.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.le_cena)

        self.button_save_danie = QPushButton(self.frame)
        self.button_save_danie.setObjectName(u"button_save_danie")
        self.button_save_danie.setStyleSheet(u"QPushButton{\n"
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
        self.button_save_danie.setIcon(icon)
        self.button_save_danie.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.button_save_danie)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(New_transaction)

        self.cb_category.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(New_transaction)
    # setupUi

    def retranslateUi(self, New_transaction):
        New_transaction.setWindowTitle(QCoreApplication.translate("New_transaction", u"New Transaction", None))
        self.le_title.setText(QCoreApplication.translate("New_transaction", u"Nowe danie", None))
        self.cb_category.setPlaceholderText(QCoreApplication.translate("New_transaction", u"Wybra\u0107 kategorie", None))
        self.le_name.setText("")
        self.le_name.setPlaceholderText(QCoreApplication.translate("New_transaction", u"Nazwa dania", None))
        self.le_description.setText("")
        self.le_description.setPlaceholderText(QCoreApplication.translate("New_transaction", u"Sklad(opis)", None))
        self.le_description_eng.setText("")
        self.le_description_eng.setPlaceholderText(QCoreApplication.translate("New_transaction", u"Sklad(opis) po angielsku", None))
        self.le_masa.setPlaceholderText(QCoreApplication.translate("New_transaction", u"Masa", None))
        self.le_cena.setPlaceholderText(QCoreApplication.translate("New_transaction", u"Cena", None))
        self.button_save_danie.setText(QCoreApplication.translate("New_transaction", u"Doda\u0107 danie", None))
    # retranslateUi

