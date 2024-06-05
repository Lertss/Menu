from models.database import Session
from models.dish_state import Dodatki
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


class DodatkiList(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lista ketegorij")

        layout = QVBoxLayout(self)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.session = Session()

        self.load_data()

        self.button_save = QPushButton("Zapisać zmiany")
        layout.addWidget(self.button_save)
        self.button_save.clicked.connect(self.save_changes)

        self.list_widget.setDragDropMode(QListWidget.InternalMove)
        self.list_widget.itemSelectionChanged.connect(self.selection_changed)

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
        data = self.session.query(Dodatki).order_by(Dodatki.text_eng).all()

        for item in data:
            list_item = QListWidgetItem(self.list_widget)
            list_item_widget = QWidget()

            layout = QHBoxLayout()
            layout.addWidget(QLabel(item.text))
            delete_button = QPushButton("Usuń")
            delete_button.clicked.connect(lambda checked=None, item=item: self.delete_item(item))
            layout.addWidget(delete_button)
            list_item_widget.setLayout(layout)

            list_item.setSizeHint(list_item_widget.sizeHint())
            self.list_widget.setItemWidget(list_item, list_item_widget)

        self.session.close()

    def delete_item(self, item):
        with self.session.begin():
            self.session.delete(item)

        for i in range(self.list_widget.count()):
            list_item = self.list_widget.item(i)
            if self.list_widget.itemWidget(list_item).findChild(QLabel).text() == item.text:
                self.list_widget.takeItem(i)
                break

        self.session.close()

    def save_changes(self):
        with self.session.begin():
            data = self.session.query(Dodatki).order_by(Dodatki.text_eng).all()
            max_turn_number = len(data)

            for index, item in enumerate(data):
                item.turn_number = max_turn_number + index + 1

        self.session.close()

    def selection_changed(self):
        current_item = self.list_widget.currentItem()
        if current_item and self.last_selected_item and current_item != self.last_selected_item:
            self.save_changes()
        self.last_selected_item = current_item
        self.session.close()
