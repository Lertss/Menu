# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dishwidget_info.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QGridLayout, QGroupBox, QHBoxLayout, QLabel, QVBoxLayout


class Ui_DishWidgetInfo(object):
    def setupUi(self, DishWidgetInfo):
        if not DishWidgetInfo.objectName():
            DishWidgetInfo.setObjectName("DishWidgetInfo")
        DishWidgetInfo.resize(400, 201)
        self.gridLayout = QGridLayout(DishWidgetInfo)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.qlb_danie = QLabel(DishWidgetInfo)
        self.qlb_danie.setObjectName("qlb_danie")
        self.qlb_danie.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.qlb_danie.setFont(font)
        self.qlb_danie.setStyleSheet("background-color: rgb(222, 222, 222);")

        self.horizontalLayout.addWidget(self.qlb_danie)

        self.qlb_cena = QLabel(DishWidgetInfo)
        self.qlb_cena.setObjectName("qlb_cena")
        self.qlb_cena.setMaximumSize(QSize(60, 40))
        self.qlb_cena.setFont(font)
        self.qlb_cena.setStyleSheet("background-color: rgb(222, 222, 222);")

        self.horizontalLayout.addWidget(self.qlb_cena)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.groupBox = QGroupBox(DishWidgetInfo)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.qlb_category = QLabel(self.groupBox)
        self.qlb_category.setObjectName("qlb_category")
        self.qlb_category.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(10)
        self.qlb_category.setFont(font1)

        self.verticalLayout.addWidget(self.qlb_category)

        self.qlb_masa = QLabel(self.groupBox)
        self.qlb_masa.setObjectName("qlb_masa")
        self.qlb_masa.setMaximumSize(QSize(16777215, 30))
        self.qlb_masa.setFont(font1)
        self.qlb_masa.setStyleSheet("\\")

        self.verticalLayout.addWidget(self.qlb_masa)

        self.qlb_des = QLabel(self.groupBox)
        self.qlb_des.setObjectName("qlb_des")
        self.qlb_des.setMaximumSize(QSize(16777215, 30))
        self.qlb_des.setFont(font1)

        self.verticalLayout.addWidget(self.qlb_des)

        self.qlb_des_eng = QLabel(self.groupBox)
        self.qlb_des_eng.setObjectName("qlb_des_eng")
        self.qlb_des_eng.setMaximumSize(QSize(16777215, 40))
        self.qlb_des_eng.setFont(font1)

        self.verticalLayout.addWidget(self.qlb_des_eng)

        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.retranslateUi(DishWidgetInfo)

        QMetaObject.connectSlotsByName(DishWidgetInfo)

    # setupUi

    def retranslateUi(self, DishWidgetInfo):
        DishWidgetInfo.setWindowTitle(
            QCoreApplication.translate("DishWidgetInfo", "Dialog", None)
        )
        self.qlb_danie.setText(
            QCoreApplication.translate("DishWidgetInfo", "Danie", None)
        )
        self.qlb_cena.setText(
            QCoreApplication.translate("DishWidgetInfo", "Cena", None)
        )
        self.groupBox.setTitle(
            QCoreApplication.translate("DishWidgetInfo", "Opis", None)
        )
        self.qlb_category.setText(
            QCoreApplication.translate("DishWidgetInfo", "Kategoria", None)
        )
        self.qlb_masa.setText(
            QCoreApplication.translate("DishWidgetInfo", "Ilo\u015b\u0107", None)
        )
        self.qlb_des.setText(QCoreApplication.translate("DishWidgetInfo", "Opis", None))
        self.qlb_des_eng.setText(
            QCoreApplication.translate("DishWidgetInfo", "Opis po angelsku", None)
        )

    # retranslateUi
