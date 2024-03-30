from PySide6.QtWidgets import QApplication, QDialog, QListWidget, QVBoxLayout, QWidget, QPushButton, QListWidgetItem, QAbstractItemView, QLabel, QHBoxLayout
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QVBoxLayout, QWidget, QPushButton


import sqlite3

class Category_list(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Список з можливістю зміни")

        layout = QVBoxLayout(self)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.load_data()  # Завантаження даних з бази даних

        self.button_save = QPushButton("Зберегти зміни")
        layout.addWidget(self.button_save)
        self.button_save.clicked.connect(self.save_changes)

        # Дозволяємо перетягувати елементи в QListWidget
        self.list_widget.setDragDropMode(QListWidget.InternalMove)

        # Відстеження вибору елемента для визначення переміщення
        self.list_widget.itemSelectionChanged.connect(self.selection_changed)

        # Збереження останнього вибраного елемента
        self.last_selected_item = None

        # Налаштування вигляду вікна
        self.setStyleSheet("""
            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,
            stop:0 rgba(128, 128, 128, 255), /* Світло-сірий */
            stop:0.427447 rgba(105, 105, 105, 235), /* Сірий */
            stop:1 rgba(84, 84, 84, 255) /* Темно-сірий */
            );
        """)

        # Налаштування вигляду QListWidget
        self.list_widget.setStyleSheet("""
            QListWidget {
                background-color: rgba(255, 255, 255, 30);
                border: 1px solid rgba(255,255,255,40);
                border-radius: 7px;
            }
            QListWidget::item {
                font-size: 16pt;
                color: white;
                padding-left: 10px;
                border: 1px solid rgba(255,255,255,40);
            }
        """)

        # Налаштування вигляду кнопки
        self.button_save.setStyleSheet("""
            QPushButton{
                color: rgb(255, 255, 255);
                background-color:rgba(255,255,255,30);
                border: 1px solid rgba(255,255,255,40);
                border-radius:7px;
                width: 230;
                height: 50;
            }
            QPushButton:hover{
                background-color:rgba(255,255,255,40);
            }
            QPushButton:pressed{
                background-color:rgba(255,255,255,70);
            }
        """)

    def load_data(self):
        # З'єднання з базою даних
        with sqlite3.connect('application.sqlite') as connection:
            cursor = connection.cursor()

            # Отримання даних з бази даних
            cursor.execute("SELECT category_name, turn_number FROM category ORDER BY turn_number")
            data = cursor.fetchall()

            # Заповнення QListWidget
            for item in data:
                list_item = QListWidgetItem(self.list_widget)
                list_item_widget = QWidget()

                layout = QHBoxLayout()
                layout.addWidget(QLabel(item[0]))
                delete_button = QPushButton("Видалити")
                delete_button.clicked.connect(lambda checked=None, item=item: self.delete_item(item))
                layout.addWidget(delete_button)
                list_item_widget.setLayout(layout)

                list_item.setSizeHint(list_item_widget.sizeHint())
                self.list_widget.setItemWidget(list_item, list_item_widget)

    def delete_item(self, item):
        # З'єднання з базою даних
        with sqlite3.connect('application.sqlite') as connection:
            cursor = connection.cursor()

            # Видалення елемента з бази даних
            cursor.execute("DELETE FROM category WHERE category_name = ?", (item[0],))

            # Збереження змін
            connection.commit()

        # Видалення елемента з QListWidget
        for i in range(self.list_widget.count()):
            list_item = self.list_widget.item(i)
            if self.list_widget.itemWidget(list_item).findChild(QLabel).text() == item[0]:
                self.list_widget.takeItem(i)
                break

    def save_changes(self):
        # З'єднання з базою даних
        with sqlite3.connect('application.sqlite') as connection:
            cursor = connection.cursor()

            # Отримання даних з QListWidget та оновлення бази даних
            for index in range(self.list_widget.count()):
                item_name = self.list_widget.itemWidget(self.list_widget.item(index)).findChild(QLabel).text()
                cursor.execute("UPDATE category SET turn_number = ? WHERE category_name = ?", (index, item_name))

            # Збереження змін
            connection.commit()

    def selection_changed(self):
        # Викликається, коли вибір елемента змінюється
        current_item = self.list_widget.currentItem()
        if current_item and self.last_selected_item and current_item != self.last_selected_item:
            self.save_changes()  # Збереження змін, якщо вибраний елемент змінився
        self.last_selected_item = current_item

