import os
import sys

from PySide6.QtWidgets import QApplication

from models.database import DATABASE_NAME, Session
from models.database_worker import create_database, Worker

from ui.mainwindow import MainWindow

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        create_database()

    app = QApplication()
    window = MainWindow(Worker(Session()))
    window.show()
    sys.exit(app.exec())