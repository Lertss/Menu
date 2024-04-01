import os
import sys

from PySide6.QtWidgets import QApplication

from models.database import DATABASE_NAME, Session
from models.database_worker import create_database, Worker
from service.service import create_folders, trim_log_file

from ui.mainwindow import MainWindow
import logging
import os

logging.basicConfig(filename='Folder/LOG/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    encoding='utf-8')
if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        create_database()

    trim_log_file()
    logging.info("Start")

    create_folders()

    app = QApplication()
    window = MainWindow(Worker(Session()))
    window.show()
    sys.exit(app.exec())
