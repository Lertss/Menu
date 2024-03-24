# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_casewidget_info.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_CaseWidgetInfo(object):
    def setupUi(self, CaseWidgetInfo):
        if not CaseWidgetInfo.objectName():
            CaseWidgetInfo.setObjectName(u"CaseWidgetInfo")
        CaseWidgetInfo.resize(400, 300)
        self.gridLayout = QGridLayout(CaseWidgetInfo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.qlb_danie = QLabel(CaseWidgetInfo)
        self.qlb_danie.setObjectName(u"qlb_danie")
        self.qlb_danie.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.qlb_danie.setFont(font)
        self.qlb_danie.setStyleSheet(u"background-color: rgb(222, 222, 222);")

        self.horizontalLayout.addWidget(self.qlb_danie)

        self.qlb_cena = QLabel(CaseWidgetInfo)
        self.qlb_cena.setObjectName(u"qlb_cena")
        self.qlb_cena.setMaximumSize(QSize(60, 40))
        self.qlb_cena.setFont(font)
        self.qlb_cena.setStyleSheet(u"background-color: rgb(222, 222, 222);")

        self.horizontalLayout.addWidget(self.qlb_cena)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.qlb_danie_eng = QLabel(CaseWidgetInfo)
        self.qlb_danie_eng.setObjectName(u"qlb_danie_eng")
        self.qlb_danie_eng.setMaximumSize(QSize(16777215, 40))
        self.qlb_danie_eng.setStyleSheet(u"background-color: rgb(222, 222, 222);")

        self.gridLayout.addWidget(self.qlb_danie_eng, 1, 0, 1, 1)

        self.groupBox = QGroupBox(CaseWidgetInfo)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.qlb_category = QLabel(self.groupBox)
        self.qlb_category.setObjectName(u"qlb_category")
        self.qlb_category.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(10)
        self.qlb_category.setFont(font1)

        self.verticalLayout.addWidget(self.qlb_category)

        self.qlb_masa = QLabel(self.groupBox)
        self.qlb_masa.setObjectName(u"qlb_masa")
        self.qlb_masa.setMaximumSize(QSize(16777215, 30))
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
        self.qlb_des_eng.setMaximumSize(QSize(16777215, 40))
        self.qlb_des_eng.setFont(font1)

        self.verticalLayout.addWidget(self.qlb_des_eng)


        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 1)


        self.retranslateUi(CaseWidgetInfo)

        QMetaObject.connectSlotsByName(CaseWidgetInfo)
    # setupUi

    def retranslateUi(self, CaseWidgetInfo):
        CaseWidgetInfo.setWindowTitle(QCoreApplication.translate("CaseWidgetInfo", u"Dialog", None))
        self.qlb_danie.setText(QCoreApplication.translate("CaseWidgetInfo", u"Danie", None))
        self.qlb_cena.setText(QCoreApplication.translate("CaseWidgetInfo", u"Cena", None))
        self.qlb_danie_eng.setText(QCoreApplication.translate("CaseWidgetInfo", u"Danie po angielsku", None))
        self.groupBox.setTitle(QCoreApplication.translate("CaseWidgetInfo", u"Opis", None))
        self.qlb_category.setText(QCoreApplication.translate("CaseWidgetInfo", u"Kategoria", None))
        self.qlb_masa.setText(QCoreApplication.translate("CaseWidgetInfo", u"Ilo\u015b\u0107", None))
        self.qlb_des.setText(QCoreApplication.translate("CaseWidgetInfo", u"Opis", None))
        self.qlb_des_eng.setText(QCoreApplication.translate("CaseWidgetInfo", u"Opis po angelsku", None))
    # retranslateUi

