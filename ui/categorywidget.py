from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from models.database import Session
from models.dish_state import Category


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

        self.setStyleSheet(
            """
                    QDialog {
                        background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,
                                                          stop:0 rgba(180, 180, 180, 255),
                                                          stop:0.427447 rgba(150, 150, 150, 235),
                                                          stop:1 rgba(110, 110, 110, 255)
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
                """
        )

        # Customize the appearance of the button
        self.button_save.setStyleSheet(
            """
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
        """
        )

    def load_data(self):
        # Connecting to the database
        # Create a new session
        with Session() as session:
            # Querying the database for category_name and turn_number from the Category table
            data = session.query(Category.category_name, Category.turn_number) \
                .order_by(Category.turn_number) \
                .all()

            # Filling the QListWidget
            for item in data:
                list_item = QListWidgetItem(self.list_widget)
                list_item_widget = QWidget()

                layout = QHBoxLayout()
                layout.addWidget(QLabel(item[0]))
                delete_button = QPushButton("Usuń")
                delete_button.clicked.connect(
                    lambda checked=None, item=item: self.delete_item(item)
                )
                layout.addWidget(delete_button)
                list_item_widget.setLayout(layout)

                list_item.setSizeHint(list_item_widget.sizeHint())
                self.list_widget.setItemWidget(list_item, list_item_widget)

    def delete_item(self, item):
        # Start a new session
        with Session() as session:
            # Query for the category by name
            category_to_delete = session.query(Category).filter(Category.category_name == item[0]).first()

            # If category is found, delete it
            if category_to_delete:
                session.delete(category_to_delete)
                session.commit()

        # Remove the item from the QListWidget
        for i in range(self.list_widget.count()):
            list_item = self.list_widget.item(i)
            if self.list_widget.itemWidget(list_item).findChild(QLabel).text() == item[0]:
                self.list_widget.takeItem(i)
                break

    def save_changes(self):
        # Start a new session
        with Session() as session:
            # Get the maximum turn_number value in the database
            max_turn_number = session.query(Category.turn_number).order_by(Category.turn_number.desc()).first()
            max_turn_number = max_turn_number[0] if max_turn_number else 0

            # If the maximum value reaches 1000, reset turn_number values
            if max_turn_number >= 999:
                for index in range(self.list_widget.count()):
                    item_name = self.list_widget.itemWidget(self.list_widget.item(index)).findChild(QLabel).text()

                    # Update turn_number based on the item's position in the list
                    category_to_update = session.query(Category).filter(Category.category_name == item_name).first()
                    if category_to_update:
                        category_to_update.turn_number = index + 1
            else:
                # Update the turn_number by incrementing based on the maximum value
                for index in range(self.list_widget.count()):
                    item_name = self.list_widget.itemWidget(self.list_widget.item(index)).findChild(QLabel).text()

                    # Update turn_number with max_turn_number + index
                    category_to_update = session.query(Category).filter(Category.category_name == item_name).first()
                    if category_to_update:
                        category_to_update.turn_number = max_turn_number + index + 1

            # Commit the changes
            session.commit()

    def selection_changed(self):
        # Called when the item selection is changed
        current_item = self.list_widget.currentItem()
        if current_item and self.last_selected_item and current_item != self.last_selected_item:
            self.save_changes()  # Save changes if the selected item has changed
        self.last_selected_item = current_item