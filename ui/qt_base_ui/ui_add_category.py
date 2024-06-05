# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_add_category.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(286, 342)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,\n"
"  stop:0 rgba(128, 128, 128, 255), /* \u0421\u0432\u0456\u0442\u043b\u043e-\u0441\u0456\u0440\u0438\u0439 */\n"
"  stop:0.427447 rgba(105, 105, 105, 235), /* \u0421\u0456\u0440\u0438\u0439 */\n"
"  stop:1 rgba(84, 84, 84, 255) /* \u0422\u0435\u043c\u043d\u043e-\u0441\u0456\u0440\u0438\u0439 */\n"
");\n"
"")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 263, 271))
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

        self.le_category = QLineEdit(self.frame)
        self.le_category.setObjectName(u"le_category")
        self.le_category.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.le_category)

        self.le_category_eng = QLineEdit(self.frame)
        self.le_category_eng.setObjectName(u"le_category_eng")
        self.le_category_eng.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.le_category_eng)

        self.le_measurement = QLineEdit(self.frame)
        self.le_measurement.setObjectName(u"le_measurement")
        self.le_measurement.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.le_measurement)

        self.button_save_category = QPushButton(self.frame)
        self.button_save_category.setObjectName(u"button_save_category")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(False)
        self.button_save_category.setFont(font1)
        self.button_save_category.setStyleSheet(u"QPushButton{\n"
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
        self.button_save_category.setIcon(icon)
        self.button_save_category.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.button_save_category)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.le_title.setText(QCoreApplication.translate("Dialog", u"Dodawanie kategorii", None))
        self.le_category.setText("")
        self.le_category.setPlaceholderText(QCoreApplication.translate("Dialog", u"Categoria", None))
        self.le_category_eng.setText("")
        self.le_category_eng.setPlaceholderText(QCoreApplication.translate("Dialog", u"Categoria po angelsku", None))
        self.le_measurement.setText("")
        self.le_measurement.setPlaceholderText(QCoreApplication.translate("Dialog", u"Typ pomiaru", None))
        self.button_save_category.setText(QCoreApplication.translate("Dialog", u"Doda\u0107 kategorie", None))
    # retranslateUi

