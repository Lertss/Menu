# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(741, 607)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(9, 9, 731, 591))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_add_category = QPushButton(self.layoutWidget)
        self.btn_add_category.setObjectName(u"btn_add_category")

        self.horizontalLayout_2.addWidget(self.btn_add_category)

        self.btn_add_danie = QPushButton(self.layoutWidget)
        self.btn_add_danie.setObjectName(u"btn_add_danie")

        self.horizontalLayout_2.addWidget(self.btn_add_danie)

        self.btn_print = QPushButton(self.layoutWidget)
        self.btn_print.setObjectName(u"btn_print")
        font = QFont()
        font.setBold(True)
        self.btn_print.setFont(font)

        self.horizontalLayout_2.addWidget(self.btn_print)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.todoListLayout = QHBoxLayout()
        self.todoListLayout.setObjectName(u"todoListLayout")

        self.verticalLayout.addLayout(self.todoListLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_add_category.setText(QCoreApplication.translate("MainWindow", u"Doda\u0107 kategorie", None))
        self.btn_add_danie.setText(QCoreApplication.translate("MainWindow", u"Doda\u0107 danie", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Rozdrukuj", None))
    # retranslateUi

