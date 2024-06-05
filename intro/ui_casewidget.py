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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_CaseWidget(object):
    def setupUi(self, CaseWidget):
        if not CaseWidget.objectName():
            CaseWidget.setObjectName(u"CaseWidget")
        CaseWidget.resize(691, 230)
        CaseWidget.setMinimumSize(QSize(180, 0))
        CaseWidget.setMaximumSize(QSize(16777215, 230))
        CaseWidget.setStyleSheet(u"\n"
"border	-radius: 10px; background-color: rgb(144, 144, 144)")
        self.gridLayout = QGridLayout(CaseWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(CaseWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"\n"
"    border: 1px solid #ccc; /* 1px \u0442\u043e\u043d\u043a\u0430 \u0440\u0430\u043c\u043a\u0430, solid \u0442\u0438\u043f \u0440\u0430\u043c\u043a\u0438, #ccc \u0441\u0456\u0440\u0438\u0439 \u043a\u043e\u043b\u0456\u0440 */\n"
"\n"
"    border-radius: 10px; /* \u0440\u0430\u0434\u0456\u0443\u0441 \u0434\u043b\u044f \u043a\u0443\u0442\u0456\u0432 */")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.qlb_danie = QLabel(self.frame)
        self.qlb_danie.setObjectName(u"qlb_danie")
        self.qlb_danie.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlb_danie.sizePolicy().hasHeightForWidth())
        self.qlb_danie.setSizePolicy(sizePolicy)
        self.qlb_danie.setMaximumSize(QSize(580, 40))
        font = QFont()
        font.setPointSize(12)
        font.setWeight(QFont.Black)
        self.qlb_danie.setFont(font)
        self.qlb_danie.setCursor(QCursor(Qt.ArrowCursor))
        self.qlb_danie.setContextMenuPolicy(Qt.NoContextMenu)
        self.qlb_danie.setStyleSheet(u"background-color: rgb(222, 222, 222);")
        self.qlb_danie.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.qlb_danie)

        self.qlb_cena = QLabel(self.frame)
        self.qlb_cena.setObjectName(u"qlb_cena")
        self.qlb_cena.setMinimumSize(QSize(0, 0))
        self.qlb_cena.setMaximumSize(QSize(60, 40))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.qlb_cena.setFont(font1)
        self.qlb_cena.setStyleSheet(u"background-color: rgb(222, 222, 222);")

        self.horizontalLayout.addWidget(self.qlb_cena)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.qlb_des = QLabel(self.frame)
        self.qlb_des.setObjectName(u"qlb_des")
        self.qlb_des.setMaximumSize(QSize(650, 30))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.qlb_des.setFont(font2)
        self.qlb_des.setStyleSheet(u"background-color: rgb(216, 216, 216);")

        self.verticalLayout.addWidget(self.qlb_des)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_info = QPushButton(self.frame)
        self.btn_info.setObjectName(u"btn_info")
        self.btn_info.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_2.addWidget(self.btn_info)

        self.btn_edit = QPushButton(self.frame)
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

        self.btn_delete = QPushButton(self.frame)
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


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)


        self.retranslateUi(CaseWidget)

        QMetaObject.connectSlotsByName(CaseWidget)
    # setupUi

    def retranslateUi(self, CaseWidget):
        CaseWidget.setWindowTitle(QCoreApplication.translate("CaseWidget", u"Form", None))
        self.qlb_danie.setText(QCoreApplication.translate("CaseWidget", u"Danie", None))
        self.qlb_cena.setText(QCoreApplication.translate("CaseWidget", u"Cena", None))
        self.qlb_des.setText(QCoreApplication.translate("CaseWidget", u"Opis ", None))
        self.btn_info.setText(QCoreApplication.translate("CaseWidget", u"Info", None))
        self.btn_edit.setText(QCoreApplication.translate("CaseWidget", u"Edytuj", None))
        self.btn_delete.setText(QCoreApplication.translate("CaseWidget", u"Usu\u0144", None))
    # retranslateUi

