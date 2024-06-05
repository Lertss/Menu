import os
import sys

from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication

from models.database import DATABASE_NAME, Session
from models.database_worker import Worker, create_database
from service.service import create_folders
from ui.mainwindow import MainWindow, style_bar_menu


def set_light_theme(app):
    palette = QPalette()

    palette.setColor(QPalette.Window, QColor(232, 232, 232))
    palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
    palette.setColor(QPalette.Base, QColor(205, 205, 205))
    palette.setColor(QPalette.AlternateBase, QColor(240, 240, 240))
    palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
    palette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))
    palette.setColor(QPalette.Text, QColor(0, 0, 0))
    palette.setColor(QPalette.Button, QColor(240, 240, 240))
    palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
    palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
    palette.setColor(QPalette.Highlight, QColor(0, 120, 215))
    palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))

    app.setPalette(palette)


if __name__ == "__main__":
    create_folders()
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        create_database()

    app = QApplication()

    app.setStyleSheet(style_bar_menu)
    set_light_theme(app)
    window = MainWindow(Worker(Session()))
    window.show()
    sys.exit(app.exec())
