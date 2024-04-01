from PySide6.QtWidgets import QApplication, QDialog, QListWidget, QVBoxLayout, QWidget, QPushButton, QListWidgetItem, QAbstractItemView, QLabel, QHBoxLayout
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QVBoxLayout, QWidget, QPushButton


import sqlite3



class Category_list(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lista kategorij")

        layout = QVBoxLayout(self)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.load_data()  # Loading data from the database

        self.button_save = QPushButton("Zapisać zmiany")
        layout.addWidget(self.button_save)
        self.button_save.clicked.connect(self.save_changes)

        # Allow to drag and drop items into a QListWidget
        self.list_widget.setDragDropMode(QListWidget.InternalMove)

        # Track item selection to determine movement
        self.list_widget.itemSelectionChanged.connect(self.selection_changed)

        # Save the last selected item
        self.last_selected_item = None

        self.setStyleSheet("""
                    QDialog {
                        background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,
                                                          stop:0 rgba(180, 180, 180, 255), /* Світло-сірий */
                                                          stop:0.427447 rgba(150, 150, 150, 235), /* Сірий */
                                                          stop:1 rgba(110, 110, 110, 255) /* Темно-сірий */
                        );
                    }

                    QListWidget {
                        background-color: rgba(255, 255, 255, 30);
                        border: 1px solid rgba(255,255,255,40);
                        border-radius: 7px;
                    }

                    QListWidget::item {
                        padding: 1px;
                        border: 1px solid rgba(0,0,0,50); 
                        color: white;
                        font-weight: bold; 
                    }

                    QPushButton {
                        color: rgb(255, 255, 255);
                        background-color: rgba(255,255,255,30);
                        border: 1px solid rgba(255,255,255,40);
                        border-radius: 7px;
                        width: 150px; 
                        height: 30px; 
                    }

                    QPushButton:hover {
                        background-color: rgba(255,255,255,40);
                    }

                    QPushButton:pressed {
                        background-color: rgba(255,255,255,70);
                    }
                """)

        # Customize the appearance of the button
        self.button_save.setStyleSheet("""
            QPushButton{
                color: rgb(255, 255, 255);
                background-color:rgba(255,255,255,30);
                border: 1px solid rgba(255,255,255,40);
                border-radius:7px;
                width: 150px;
                height: 30px;
            }
            QPushButton:hover{
                background-color:rgba(255,255,255,40);
            }
            QPushButton:pressed{
                background-color:rgba(255,255,255,70);
            }
        """)


    def load_data(self):
        # Connecting to the database
        with sqlite3.connect('application.sqlite') as connection:
            cursor = connection.cursor()

            # Retrieving data from the database
            cursor.execute("SELECT category_name, turn_number FROM category ORDER BY turn_number")
            data = cursor.fetchall()

            # Filling the QListWidget
            for item in data:
                list_item = QListWidgetItem(self.list_widget)
                list_item_widget = QWidget()

                layout = QHBoxLayout()
                layout.addWidget(QLabel(item[0]))
                delete_button = QPushButton("Usuń")
                delete_button.clicked.connect(lambda checked=None, item=item: self.delete_item(item))
                layout.addWidget(delete_button)
                list_item_widget.setLayout(layout)

                list_item.setSizeHint(list_item_widget.sizeHint())
                self.list_widget.setItemWidget(list_item, list_item_widget)

    def delete_item(self, item):
        with sqlite3.connect('application.sqlite') as connection:
            cursor = connection.cursor()

            # Deleting an item from the database
            cursor.execute("DELETE FROM category WHERE category_name = ?", (item[0],))
            connection.commit()

        # Removing an item from a QListWidget
        for i in range(self.list_widget.count()):
            list_item = self.list_widget.item(i)
            if self.list_widget.itemWidget(list_item).findChild(QLabel).text() == item[0]:
                self.list_widget.takeItem(i)
                break

    def save_changes(self):
        with sqlite3.connect('application.sqlite') as connection:
            cursor = connection.cursor()

            # Get the maximum turn_number value in the database
            cursor.execute("SELECT MAX(turn_number) FROM category")
            max_turn_number = cursor.fetchone()[0] or 0  # Якщо MAX(turn_number) повертає None, встановити 0

            # If the maximum value reaches 1000, overwrite all turn_number values
            if max_turn_number >= 999:
                for index in range(self.list_widget.count()):
                    item_name = self.list_widget.itemWidget(self.list_widget.item(index)).findChild(QLabel).text()

                    # Update turn_number based on item position in the list
                    cursor.execute("UPDATE category SET turn_number = ? WHERE category_name = ?",
                                   (index + 1, item_name))
            else:
                # Update the turn_number value for each item
                for index in range(self.list_widget.count()):
                    item_name = self.list_widget.itemWidget(self.list_widget.item(index)).findChild(QLabel).text()

                    # Update turn_number by increasing the maximum value by 1
                    cursor.execute("UPDATE category SET turn_number = ? WHERE category_name = ?",
                                   (max_turn_number + index + 1, item_name))

            connection.commit()

    def selection_changed(self):
        # Called when the item selection is changed
        current_item = self.list_widget.currentItem()
        if current_item and self.last_selected_item and current_item != self.last_selected_item:
            self.save_changes()  # Save changes if the selected item has changed
        self.last_selected_item = current_item

