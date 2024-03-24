from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget

from models.case_state import Category
from models.database import Session
from models.case import Case
from intro.ui_casewidget import Ui_CaseWidget
from intro.ui_casewidget_info import Ui_CaseWidgetInfo
from models.database_worker import Worker
from ui.qt_base_ui.ui_new_transaction import Ui_New_transaction


class CaseWidget(QWidget):

    def __init__(self, data: Case, case_list_widget):
        super(CaseWidget, self).__init__()
        self.data = data
        self.worker = Worker
        self.case_list_widget = case_list_widget
        self.ui = Ui_CaseWidget()
        self.ui.setupUi(self)
        self.ui.qlb_danie.setText(data.name)
        self.ui.qlb_des.setText(data.description)
        self.ui.qlb_cena.setText(str(data.price) + " pl")
        self.ui.btn_delete.clicked.connect(self.delete_case)
        self.ui.btn_edit.clicked.connect(self.open_update_window)
        self.ui.btn_info.clicked.connect(self.open_info_window)

    def delete_case(self):
        Case.delete_case(self.data.id)
        self.case_list_widget.reloads()

    def open_update_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_New_transaction()
        self.ui_window.setupUi(self.new_window)
        options = []
        categories = self.worker.getCategories()

        # Виведення всіх категорій
        for category in categories:
            options.append(category.category_name)

        self.ui_window.cb_category.addItems(options)
        self.new_window.show()
        self.ui_window.button_save_danie.clicked.connect(self.update_window)

    def update_window(self):
        id = self.data.id
        category = self.ui_window.cb_category.currentIndex() + 1
        name = self.ui_window.le_name.text()
        name_eng = self.ui_window.le_name_eng.text()
        description = self.ui_window.le_description.text()
        description_eng = self.ui_window.le_description_eng.text()
        masa = self.ui_window.le_masa.text()
        cena = self.ui_window.le_cena.text()

        Case.update_case(id, category, name, name_eng, description, description_eng, masa, cena)

        # Оновлюємо дані у віджеті
        self.reload_data()

        # Оновлюємо список віджетів
        self.case_list_widget.reloads()

        # Закриваємо вікно оновлення
        self.new_window.close()

    def reload_data(self):
        # Отримання оновлених даних з бази даних
        session = Session()
        updated_data = session.query(Case).filter_by(id=self.data.id).first()
        session.close()

        # Оновлення даних та UI віджету
        self.data = updated_data
        self.ui.qlb_danie.setText(self.data.name)
        self.ui.qlb_des.setText(self.data.description)
        self.ui.qlb_cena.setText(str(self.data.price) + " pl")

    def open_info_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_CaseWidgetInfo()
        self.ui_window.setupUi(self.new_window)

        # Assuming self.data is available and contains necessary attributes
        self.ui_window.qlb_danie.setText(self.data.name)
        self.ui_window.qlb_danie_eng.setText(self.data.name_eng)
        self.ui_window.qlb_des.setText(self.data.description)
        self.ui_window.qlb_des_eng.setText(self.data.description_english)
        self.ui_window.qlb_cena.setText(str(self.data.price) + " pl")

        category = self.case_list_widget.worker.session.query(Category).filter_by(id=self.data.category).first()
        if category:
            self.ui_window.qlb_category.setText(category.category_name)
            self.ui_window.qlb_masa.setText(str(self.data.masa) + " " + category.pomiar)
        else:
            self.ui_window.qlb_category.setText("No Category")

        self.new_window.show()

        print(1)
        # print(self.data.category_name)


