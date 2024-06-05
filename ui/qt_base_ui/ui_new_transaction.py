# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_new_transaction.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)


class Ui_New_transaction(object):
    def setupUi(self, New_transaction):
        if not New_transaction.objectName():
            New_transaction.setObjectName("New_transaction")
        New_transaction.resize(477, 436)
        New_transaction.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,\n"
            "  stop:0 rgba(128, 128, 128, 255), /* \u0421\u0432\u0456\u0442\u043b\u043e-"
            "\u0441\u0456\u0440\u0438\u0439 */\n"
            "  stop:0.427447 rgba(85, 85, 85, 235), /* \u0421\u0456\u0440\u0438\u0439 */\n"
            "  stop:1 rgba(64, 64, 64, 255) /* \u0422\u0435\u043c\u043d\u043e-\u0441\u0456\u0440\u0438\u0439 */\n"
            ");\n"
            ""
        )
        self.horizontalLayout = QHBoxLayout(New_transaction)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QFrame(New_transaction)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet(
            "background-color: rgba(255, 255, 255, 30);\n"
            "border: 1px solid rgba(255,255,255,40);\n"
            "border-radius: 7px;"
        )
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.le_title = QLabel(self.frame)
        self.le_title.setObjectName("le_title")
        self.le_title.setMaximumSize(QSize(16777215, 70))
        self.le_title.setStyleSheet(
            "color: white;\n"
            "font-weight: bold;\n"
            "font-size: 20pt;\n"
            "background-color: none;\n"
            "border: none;\n"
            ""
        )
        self.le_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.le_title)

        self.cb_category = QComboBox(self.frame)
        self.cb_category.setObjectName("cb_category")
        self.cb_category.setStyleSheet(
            "QComboBox {\n"
            "font-size: 16pt;\n"
            "color: white;\n"
            "}\n"
            "\n"
            "QComboBox:item {\n"
            "    color: black;\n"
            "}"
        )

        self.verticalLayout.addWidget(self.cb_category)

        self.le_name = QLineEdit(self.frame)
        self.le_name.setObjectName("le_name")
        self.le_name.setStyleSheet(
            "font-size: 16pt;\n" "color: white;\n" "padding-left: 10px;"
        )

        self.verticalLayout.addWidget(self.le_name)

        self.le_description = QLineEdit(self.frame)
        self.le_description.setObjectName("le_description")
        self.le_description.setStyleSheet(
            "font-size: 16pt;\n" "color: white;\n" "padding-left: 10px;"
        )

        self.verticalLayout.addWidget(self.le_description)

        self.le_description_eng = QLineEdit(self.frame)
        self.le_description_eng.setObjectName("le_description_eng")
        self.le_description_eng.setStyleSheet(
            "font-size: 16pt;\n" "color: white;\n" "padding-left: 10px;"
        )

        self.verticalLayout.addWidget(self.le_description_eng)

        self.le_masa = QLineEdit(self.frame)
        self.le_masa.setObjectName("le_masa")
        self.le_masa.setStyleSheet(
            "font-size: 16pt;\n" "color: white;\n" "padding-left: 10px;"
        )

        self.verticalLayout.addWidget(self.le_masa)

        self.le_cena = QLineEdit(self.frame)
        self.le_cena.setObjectName("le_cena")
        self.le_cena.setStyleSheet(
            "font-size: 16pt;\n" "color: white;\n" "padding-left: 10px;"
        )

        self.verticalLayout.addWidget(self.le_cena)

        self.button_save_danie = QPushButton(self.frame)
        self.button_save_danie.setObjectName("button_save_danie")
        self.button_save_danie.setStyleSheet(
            "QPushButton{\n"
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
            "}"
        )
        icon = QIcon()
        icon.addFile(
            ":/icons/icons/post_add_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.button_save_danie.setIcon(icon)
        self.button_save_danie.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.button_save_danie)

        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(New_transaction)

        self.cb_category.setCurrentIndex(-1)

        QMetaObject.connectSlotsByName(New_transaction)

    # setupUi

    def retranslateUi(self, New_transaction):
        New_transaction.setWindowTitle(
            QCoreApplication.translate("New_transaction", "New Transaction", None)
        )
        self.le_title.setText(
            QCoreApplication.translate("New_transaction", "Nowe danie", None)
        )
        self.cb_category.setPlaceholderText(
            QCoreApplication.translate("New_transaction", "Kategoria", None)
        )
        self.le_name.setText("")
        self.le_name.setPlaceholderText(
            QCoreApplication.translate("New_transaction", "Nazwa dania", None)
        )
        self.le_description.setText("")
        self.le_description.setPlaceholderText(
            QCoreApplication.translate("New_transaction", "Sklad(opis)", None)
        )
        self.le_description_eng.setText("")
        self.le_description_eng.setPlaceholderText(
            QCoreApplication.translate(
                "New_transaction", "Sklad(opis) po angielsku", None
            )
        )
        self.le_masa.setPlaceholderText(
            QCoreApplication.translate("New_transaction", "Masa", None)
        )
        self.le_cena.setPlaceholderText(
            QCoreApplication.translate("New_transaction", "Cena", None)
        )
        self.button_save_danie.setText(
            QCoreApplication.translate("New_transaction", "Zapisz", None)
        )

    # retranslateUi
