from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QBrush, QColor, QPainter
from PySide6.QtWidgets import QAbstractItemView, QListWidget, QListWidgetItem, QWidget

from models.database_worker import Worker
from models.dish import Dish
from models.dish_state import DishState
from ui.dishwidget import DishWidget
from ui.qt_base_ui.ui_todolist import Ui_Form


class MyListWidget(QListWidget):
    def __init__(self, id_state: int, parent=None):
        super(MyListWidget, self).__init__(parent)
        self.id_state = id_state
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setDefaultDropAction(Qt.MoveAction)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setAcceptDrops(True)
        self.model().rowsInserted.connect(self.handleRowsInserted, Qt.QueuedConnection)

    def handleRowsInserted(self, parent, first, last):
        for it in range(first, last + 1):
            item = self.item(it)
            if item is not None and self.itemWidget(item) is None:
                data = item.data(Qt.UserRole)
                if data.dish_state != self.id_state:
                    data.dish_state = self.id_state
                    data.update_state()
                # Pass the DishListWidget instance to DishWidget
                widget = DishWidget(data, self.parentWidget().parentWidget())
                item.setSizeHint(widget.sizeHint())
                self.setItemWidget(item, widget)


class DishListWidget(QWidget):
    def __init__(self, dish_state: DishState, worker: Worker):
        super(DishListWidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.dish_state = dish_state
        self.worker = worker
        self.ui.groupBox.setTitle(dish_state.dish_state_name)
        self.listWidget = MyListWidget(self.dish_state.id, self)
        self.ui.todoListLayout.addWidget(self.listWidget)
        self.reloads()

    def paintEvent(self, event):
        painter = QPainter(self)

        # Background.
        painter.setBrush(QBrush(QColor(185, 185, 185)))
        painter.drawRect(QRect(0, 0, self.width(), self.height()))

    def reloads(self):
        self.listWidget.clear()
        for it in self.worker.getDishs(self.dish_state):
            self._add_widget(it)

    def _add_widget(self, dish: Dish):
        my_item = QListWidgetItem(self.listWidget)
        my_item.setData(Qt.UserRole, dish)
        self.listWidget.addItem(my_item)
