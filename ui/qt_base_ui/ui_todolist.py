# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_todolist.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QGroupBox, QVBoxLayout


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(380, 448)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        Form.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.todoListLayout = QVBoxLayout()
        self.todoListLayout.setObjectName("todoListLayout")

        self.verticalLayout.addLayout(self.todoListLayout)

        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", "GroupBox", None))

    # retranslateUi
