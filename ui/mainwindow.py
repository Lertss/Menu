import PySide6
from PySide6 import QtWidgets
from PySide6.QtGui import QAction, QIntValidator, QDoubleValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox
from sqlalchemy import func

from generate_html import generation_pdf
from intro.ui_dodawanie_dodatkow import Ui_new_Dodatek

from models.case import Case
from models.database import Session
from models.database_worker import Worker
from ui.categorywidget import Category_list
from ui.dodatkiwidget import DodatkiList
from ui.qt_base_ui.ui_add_category import Ui_Dialog
from intro.ui_mainwindow import Ui_MainWindow
from ui.caselistwidget import CaseListWidget
from models.case_state import Category, Dodatki
from ui.qt_base_ui.ui_new_transaction import Ui_New_transaction


class MainWindow(QMainWindow):
    def __init__(self, worker: Worker):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.worker = worker
        self.initUI()
        for it in worker.getStates():
            self.ui.todoListLayout.addWidget(CaseListWidget(it, worker))

    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Kategorie')

        func1Action = QAction('Dodać kategorie', self)
        func1Action.triggered.connect(self.open_new_category_window)

        func2Action = QAction('Lista kategorij', self)
        func2Action.triggered.connect(self.open_category_list_window)

        fileMenu.addAction(func1Action)
        fileMenu.addAction(func2Action)

        fileMenu = menubar.addMenu('Dodatki')

        func5Action = QAction('Dodać dodatek', self)
        func5Action.triggered.connect(self.open_new_dodatki_window)

        func6Action = QAction('Lista dodatków', self)
        func6Action.triggered.connect(self.open_dodatki_list_window)

        fileMenu.addAction(func5Action)
        fileMenu.addAction(func6Action)

        func3Action = QAction('Dodać danie', self)
        func3Action.triggered.connect(self.open_new_case_window)
        menubar.addAction(func3Action)

        func4Action = QAction('Stworyć zdjęcie', self)
        func4Action.triggered.connect(generation_pdf)
        menubar.addAction(func4Action)




        self.setWindowTitle('QMenuBar')
        self.show()


    def open_category_list_window(self):
        category_list_dialog = Category_list()
        category_list_dialog.resize(400, 400)
        category_list_dialog.exec_()

    def open_dodatki_list_window(self):
        category_list_dialog = DodatkiList()
        category_list_dialog.resize(400, 400)
        category_list_dialog.exec_()

    def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None:
        del self.worker

    def open_new_category_window(self):
        self.new_window_category = QtWidgets.QDialog()
        self.ui_window_category = Ui_Dialog()
        self.ui_window_category.setupUi(self.new_window_category)
        self.new_window_category.show()
        self.ui_window_category.button_save_category.clicked.connect(self.add_new_category)

    def add_new_category(self):
        category_name = self.ui_window_category.le_category.text()
        category_eng_name = self.ui_window_category.le_category_eng.text()
        measurement = self.ui_window_category.le_measurement.text()
        session = Session()
        new_category = Category(category_name=category_name,category_eng_name=category_eng_name, pomiar=measurement, turn_number=new_turn_number())
        session.add(new_category)
        session.commit()
        session.close()
        self.new_window_category.close()

    def open_new_case_window(self):
        self.new_window_case = QtWidgets.QDialog()
        self.ui_window_case = Ui_New_transaction()
        self.ui_window_case.setupUi(self.new_window_case)

        self.ui_window_case.le_masa.setValidator(QIntValidator())
        self.ui_window_case.le_cena.setValidator(QDoubleValidator())

        options = []
        categories = self.worker.getCategories()

        for category in categories:
            options.append(category.category_name)

        self.ui_window_case.cb_category.addItems(options)
        self.new_window_case.show()
        self.ui_window_case.button_save_danie.clicked.connect(self.add_new_case)

    def add_new_case(self):
        category_name = self.ui_window_case.cb_category.currentText()
        category_id = self.worker.getCategoryIdByName(category_name)
        name = self.ui_window_case.le_name.text()
        description = self.ui_window_case.le_description.text()
        description_eng = self.ui_window_case.le_description_eng.text()
        masa = self.ui_window_case.le_masa.text()
        cena = self.ui_window_case.le_cena.text()
        price_float = float(cena.replace(',', '.'))
        Case.create_case(category_id, name, description, description_eng, price_float, masa)

        for widget in self.findChildren(CaseListWidget):
            widget.reloads()

        self.new_window_case.close()

    def open_new_dodatki_window(self):
        self.new_window_dodatki = QtWidgets.QDialog()
        self.ui_window_dodatki = Ui_new_Dodatek()
        self.ui_window_dodatki.setupUi(self.new_window_dodatki)
        self.new_window_dodatki.show()
        self.ui_window_dodatki.button_save_dodatek.clicked.connect(self.add_new_dodatek)

    def add_new_dodatek(self):
        dodatki_name = self.ui_window_dodatki.dodatki.toPlainText()
        dodatki_eng_name = self.ui_window_dodatki.textEdit_eng.toPlainText()
        session = Session()
        new_dodatek = Dodatki(text=dodatki_name, text_eng=dodatki_eng_name)
        session.add(new_dodatek)
        session.commit()
        session.close()
        self.new_window_dodatki.close()


def new_turn_number():
    session = Session()
    max_turn_number = session.query(func.max(Category.turn_number)).scalar()
    session.close()
    if max_turn_number:
        if max_turn_number > 0:
            return max_turn_number +1
    else:
        return 1

