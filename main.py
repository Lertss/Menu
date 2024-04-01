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

    import logging
    import os

    # Кількість останніх логів, які будуть збережені
    MAX_LOGS = 500

    # Налаштування рівня логування та форматування
    logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                        encoding='utf-8')

    import time
    # Приклад використання

    logging.info('Це повідомлення у рівні INFO  Ó ą ę ć')
    logging.warning('Це повідомлення у рівні WARNING')
    logging.error("i")

    # Обрізання файлу логу до останніх MAX_LOGS записів



    def trim_log_file():
        try:
            with open('app.log', 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # Збереження останніх MAX_LOGS рядків
            lines = lines[-MAX_LOGS:]

            with open('app.log', 'w', encoding='utf-8') as f:
                f.writelines(lines)
        except FileNotFoundError:
            # Якщо файл не існує, нічого не робимо
            pass

    trim_log_file()

    app = QApplication()
    window = MainWindow(Worker(Session()))
    window.show()
    sys.exit(app.exec())




