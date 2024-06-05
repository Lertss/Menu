import PySide6
from PySide6 import QtWidgets
from PySide6.QtGui import QAction, QIntValidator, QDoubleValidator
from PySide6.QtWidgets import QMainWindow, QColorDialog, QLineEdit
from sqlalchemy import func

from generate_html import generation_pdf
from intro.ui_dodawanie_dodatkow import Ui_new_Dodatek
from intro.ui_mainwindow import Ui_MainWindow
from models.dish import Dish
from models.dish_state import Category, Dodatki
from models.database import Session
from models.database_worker import Worker
from service.service import save_settings, load_settings
from ui.dishlistwidget import DishListWidget
from ui.categorywidget import Category_list
from ui.dodatkiwidget import DodatkiList
from ui.qt_base_ui.ui_add_category import Ui_Dialog
from ui.qt_base_ui.ui_new_transaction import Ui_New_transaction


class MainWindow(QMainWindow):
    def __init__(self, worker: Worker):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.worker = worker
        self.settings = load_settings()
        self.initUI()

        self.search_line = QLineEdit(self)
        self.search_line.setPlaceholderText("Szukaj...")
        self.search_line.setStyleSheet("color: rgb(255, 0, 0);")
        self.search_line.textChanged.connect(self.handle_search)
        self.ui.verticalLayout.insertWidget(0, self.search_line)

        self.dish_list_widgets = []
        for it in self.worker.getStates():
            dish_list_widget = DishListWidget(it, self.worker)
            self.dish_list_widgets.append(dish_list_widget)
            self.ui.todoListLayout.addWidget(dish_list_widget)

    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Kategoria')

        func1Action = QAction('Nowa kategoria', self)
        func1Action.triggered.connect(self.open_new_category_window)

        func2Action = QAction('Lista kategorii', self)
        func2Action.triggered.connect(self.open_category_list_window)

        fileMenu.addAction(func1Action)
        fileMenu.addAction(func2Action)

        fileMenu = menubar.addMenu('Dodatki')

        func5Action = QAction('Nowy dodatek', self)
        func5Action.triggered.connect(self.open_new_dodatki_window)

        func6Action = QAction('Lista dodatków', self)
        func6Action.triggered.connect(self.open_dodatki_list_window)

        fileMenu.addAction(func5Action)
        fileMenu.addAction(func6Action)

        func3Action = QAction('Nowe danie', self)
        func3Action.triggered.connect(self.open_new_dish_window)
        menubar.addAction(func3Action)

        func4Action = QAction('Zdjęcie', self)
        func4Action.triggered.connect(generation_pdf)
        menubar.addAction(func4Action)



        # Add color picker buttons
        color_menu = menubar.addMenu('Ustawienia Koloru')

        headline_action = QAction('Kolor naglówka ', self)
        headline_action.triggered.connect(lambda: self.change_color('headline'))
        color_menu.addAction(headline_action)

        category_action = QAction('Kolor kategorij', self)
        category_action.triggered.connect(lambda: self.change_color('category'))
        color_menu.addAction(category_action)

        main_action = QAction('Kolory nazwy dania', self)
        main_action.triggered.connect(lambda: self.change_color('main'))
        color_menu.addAction(main_action)

        danie_eng_action = QAction('Kolor opisu ', self)
        danie_eng_action.triggered.connect(lambda: self.change_color('description'))
        color_menu.addAction(danie_eng_action)

        danie_eng_action = QAction('Kolor eng. nazwy dania ', self)
        danie_eng_action.triggered.connect(lambda: self.change_color('english_dish'))
        color_menu.addAction(danie_eng_action)

        masa_action = QAction('Kolor masy', self)
        masa_action.triggered.connect(lambda: self.change_color('masa'))
        color_menu.addAction(masa_action)

        cena_action = QAction('Kolor ceny', self)
        cena_action.triggered.connect(lambda: self.change_color('cena'))
        color_menu.addAction(cena_action)

        dodatki_action = QAction('Kolory dodatków', self)
        dodatki_action.triggered.connect(lambda: self.change_color('dodatki'))
        color_menu.addAction(dodatki_action)



        self.setWindowTitle('QMenuBar')
        self.show()


    def change_color(self, element):
        color = QColorDialog.getColor()
        if color.isValid():
            self.settings[element] = color.name()
            save_settings(self.settings)

    def handle_search(self, text):
        for dish_list_widget in self.dish_list_widgets:
            dish_list_widget.listWidget.clear()
            for dish in self.worker.getDishs(dish_list_widget.dish_state):
                if text.lower() in dish.name.lower() or text.lower() in dish.description.lower():
                    dish_list_widget._add_widget(dish)

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

    def open_new_dish_window(self):
        self.new_window_dish = QtWidgets.QDialog()
        self.ui_window_dish = Ui_New_transaction()
        self.ui_window_dish.setupUi(self.new_window_dish)

        self.ui_window_dish.le_masa.setValidator(QIntValidator())
        self.ui_window_dish.le_cena.setValidator(QDoubleValidator())

        options = []
        categories = self.worker.getCategories()

        for category in categories:
            options.append(category.category_name)

        self.ui_window_dish.cb_category.addItems(options)
        self.new_window_dish.show()
        self.ui_window_dish.button_save_danie.clicked.connect(self.add_new_dish)

    def add_new_dish(self):
        category_name = self.ui_window_dish.cb_category.currentText()
        category_id = self.worker.getCategoryIdByName(category_name)
        name = self.ui_window_dish.le_name.text()
        description = self.ui_window_dish.le_description.text()
        description_eng = self.ui_window_dish.le_description_eng.text()
        masa = self.ui_window_dish.le_masa.text()
        cena = self.ui_window_dish.le_cena.text()
        price_float = float(cena.replace(',', '.'))
        Dish.create_dish(category_id, name, description, description_eng, price_float, masa)

        for widget in self.findChildren(DishListWidget):
            widget.reloads()

        self.new_window_dish.close()

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

style_bar_menu = """
        QMenuBar {
            background-color: #f0f0f0;
            color: #000;
        }
        QMenuBar::item {
            background-color: #f0f0f0;
            color: #000;
        }
        QMenuBar::item:selected {
            background-color: #d0d0d0;
        }
        QMenu {
            background-color: #f0f0f0;
            color: #000;
        }
        QMenu::item:selected {
            background-color: #d0d0d0;
        }
    """
