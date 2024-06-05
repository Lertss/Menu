import locale

from intro.ui_dishwidget import Ui_DishWidget
from intro.ui_dishwidget_info import Ui_DishWidgetInfo
from models.database import Session
from models.dish import Dish
from models.dish_state import Category
from PySide6 import QtWidgets
from PySide6.QtGui import QDoubleValidator, QIntValidator
from PySide6.QtWidgets import QWidget
from ui.qt_base_ui.ui_new_transaction import Ui_New_transaction


class DishWidget(QWidget):

    def __init__(self, data: Dish, dish_list_widget):
        super(DishWidget, self).__init__()
        self.data = data
        self.dish_list_widget = dish_list_widget
        self.ui = Ui_DishWidget()
        self.ui.setupUi(self)
        self.ui.qlb_danie.setText(data.name)
        self.ui.qlb_des.setText(data.description)
        self.ui.qlb_cena.setText(str(data.price) + " pl")
        self.ui.btn_delete.clicked.connect(self.delete_dish)
        self.ui.btn_edit.clicked.connect(self.open_update_window)
        self.ui.btn_info.clicked.connect(self.open_info_window)

    def delete_dish(self):
        Dish.delete_dish(self.data.id)
        self.dish_list_widget.reloads()

    def open_update_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_New_transaction()
        self.ui_window.setupUi(self.new_window)

        # Getting a category for a Dish record
        category = self.dish_list_widget.worker.session.query(Category).filter_by(id=self.data.category).first()

        categories = self.dish_list_widget.worker.session.query(Category)

        options = []
        category_index = None
        # Displaying all categories
        for index, cat in enumerate(categories):
            options.append(cat.category_name)
            if cat.id == category.id:
                category_index = index

        self.ui_window.cb_category.addItems(options)

        if category_index is not None:
            self.ui_window.cb_category.setCurrentIndex(category_index)
        self.ui_window.le_title.setText("Aktualizacja dania")
        self.ui_window.le_name.setText(self.data.name)
        self.ui_window.le_description.setText(self.data.description)
        self.ui_window.le_description_eng.setText(self.data.description_english)
        self.ui_window.le_masa.setText(str(self.data.masa))

        # Setting the price value with a decimal point and two zeros after the decimal point
        locale.setlocale(locale.LC_NUMERIC, "")  # Setting the locale for numeric formatting
        formatted_price = locale._format("%.2f", self.data.price, grouping=True)
        self.ui_window.le_cena.setText(formatted_price)

        # Add validators for the 'cena' and 'masa' fields
        self.ui_window.le_cena.setValidator(QIntValidator())
        self.ui_window.le_cena.setValidator(QDoubleValidator(bottom=0))

        self.new_window.show()
        self.ui_window.button_save_danie.clicked.connect(self.update_window)

    def update_window(self):
        id = self.data.id
        category_id = (
            self.dish_list_widget.worker.session.query(Category)
            .filter_by(category_name=self.ui_window.cb_category.currentText())
            .first()
            .id
        )
        name = self.ui_window.le_name.text()

        description = self.ui_window.le_description.text()
        description_eng = self.ui_window.le_description_eng.text()
        masa = self.ui_window.le_masa.text()
        cena = self.ui_window.le_cena.text()
        price_float = float(cena.replace(",", "."))
        Dish.update_dish(id, category_id, name, description, description_eng, masa, price_float)

        # Update the data in the widget
        self.reload_data()

        # Update the list of widgets
        self.dish_list_widget.reloads()

        # Close the update window
        self.new_window.close()

    def reload_data(self):
        # Getting updated data from the database
        session = Session()
        updated_data = session.query(Dish).filter_by(id=self.data.id).first()
        session.close()

        # Update data and widget UI
        self.data = updated_data
        self.ui.qlb_danie.setText(self.data.name)
        self.ui.qlb_des.setText(self.data.description)
        self.ui.qlb_cena.setText(str(self.data.price) + " pl")

    def open_info_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_DishWidgetInfo()
        self.ui_window.setupUi(self.new_window)

        # Assuming self.data is available and contains necessary attributes
        self.ui_window.qlb_danie.setText(self.data.name)
        self.ui_window.qlb_des.setText(self.data.description)
        self.ui_window.qlb_des_eng.setText(self.data.description_english)
        self.ui_window.qlb_cena.setText(str(self.data.price) + " pl")

        category = self.dish_list_widget.worker.session.query(Category).filter_by(id=self.data.category).first()
        if category:
            self.ui_window.qlb_category.setText(category.category_name)
            self.ui_window.qlb_masa.setText(str(self.data.masa) + " " + category.pomiar)
        else:
            self.ui_window.qlb_category.setText("No Category")

        self.new_window.show()
