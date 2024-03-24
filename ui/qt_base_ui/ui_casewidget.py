# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_casewidget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_CaseWidget(object):
    def setupUi(self, CaseWidget):
        if not CaseWidget.objectName():
            CaseWidget.setObjectName(u"CaseWidget")
        CaseWidget.resize(392, 230)
        CaseWidget.setMinimumSize(QSize(180, 0))
        CaseWidget.setMaximumSize(QSize(16777215, 230))
        CaseWidget.setStyleSheet(u"\n"
"border	-radius: 5px;")
        self.gridLayout = QGridLayout(CaseWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(CaseWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 110))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.qlb_masa = QLabel(self.groupBox)
        self.qlb_masa.setObjectName(u"qlb_masa")
        self.qlb_masa.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(10)
        self.qlb_masa.setFont(font1)
        self.qlb_masa.setStyleSheet(u"\\")

        self.verticalLayout.addWidget(self.qlb_masa)

        self.qlb_des = QLabel(self.groupBox)
        self.qlb_des.setObjectName(u"qlb_des")
        self.qlb_des.setMaximumSize(QSize(16777215, 30))
        self.qlb_des.setFont(font1)

        self.verticalLayout.addWidget(self.qlb_des)

        self.qlb_des_eng = QLabel(self.groupBox)
        self.qlb_des_eng.setObjectName(u"qlb_des_eng")
        self.qlb_des_eng.setMaximumSize(QSize(16777215, 30))
        self.qlb_des_eng.setFont(font1)

        self.verticalLayout.addWidget(self.qlb_des_eng)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.qlb_danie = QLabel(CaseWidget)
        self.qlb_danie.setObjectName(u"qlb_danie")
        self.qlb_danie.setMaximumSize(QSize(16777215, 40))
        self.qlb_danie.setFont(font)
        self.qlb_danie.setStyleSheet(u"background-color: rgb(222, 222, 222);")

        self.horizontalLayout.addWidget(self.qlb_danie)

        self.qlb_danie_eng = QLabel(CaseWidget)
        self.qlb_danie_eng.setObjectName(u"qlb_danie_eng")
        self.qlb_danie_eng.setMaximumSize(QSize(16777215, 40))
        self.qlb_danie_eng.setStyleSheet(u"background-color: rgb(222, 222, 222);")

        self.horizontalLayout.addWidget(self.qlb_danie_eng)

        self.qlb_cena = QLabel(CaseWidget)
        self.qlb_cena.setObjectName(u"qlb_cena")
        self.qlb_cena.setMaximumSize(QSize(16777215, 40))
        self.qlb_cena.setFont(font)
        self.qlb_cena.setStyleSheet(u"background-color: rgb(222, 222, 222);")

        self.horizontalLayout.addWidget(self.qlb_cena)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_edit = QPushButton(CaseWidget)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setStyleSheet(u"QPushButton{\n"
" 	 background-color:rgba(200,200,200,90);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"	 height:30\n"
"}\n"
"QPushButton:hover{\n"
"	 background-color:rgba(209,209,209,60);\n"
"     border: 1px solid rgba(0,0,0,50);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgba(180,180,180,70);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_edit)

        self.btn_delete = QPushButton(CaseWidget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setStyleSheet(u"QPushButton{\n"
" 	 background-color:rgba(200,200,200,90);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"	 height:30\n"
"}\n"
"QPushButton:hover{\n"
"	 background-color:rgba(209,209,209,60);\n"
"     border: 1px solid rgba(0,0,0,50);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgba(180,180,180,70);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_delete)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)


        self.retranslateUi(CaseWidget)

        QMetaObject.connectSlotsByName(CaseWidget)
    # setupUi

    def retranslateUi(self, CaseWidget):
        CaseWidget.setWindowTitle(QCoreApplication.translate("CaseWidget", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("CaseWidget", u"Opis", None))
        self.qlb_masa.setText(QCoreApplication.translate("CaseWidget", u"Ilo\u015b\u0107", None))
        self.qlb_des.setText(QCoreApplication.translate("CaseWidget", u"Opis", None))
        self.qlb_des_eng.setText(QCoreApplication.translate("CaseWidget", u"Opis po angelsku", None))
        self.qlb_danie.setText(QCoreApplication.translate("CaseWidget", u"Danie", None))
        self.qlb_danie_eng.setText(QCoreApplication.translate("CaseWidget", u"Danie po angielsku", None))
        self.qlb_cena.setText(QCoreApplication.translate("CaseWidget", u"Cena", None))
        self.btn_edit.setText(QCoreApplication.translate("CaseWidget", u"Edytowa\u0107", None))
        self.btn_delete.setText(QCoreApplication.translate("CaseWidget", u"Usun\u0105\u0107", None))
    # retranslateUi

