from PySide6.QtCore import QTimer
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication
import sys


def render_html_to_image(html_file, output_image):
    app = QApplication(sys.argv)

    # Створюємо веб-движок
    web = QWebEngineView()

    # Функція для захоплення зображення
    def capture():
        # Робимо скріншот і зберігаємо зображення
        web.grab().save(output_image)
        print(f'Зображення збережено як {output_image}')
        # Закриваємо веб-движок (за бажанням)
        web.deleteLater()
        app.quit()  # Завершуємо роботу додатку після збереження зображення

    # Підключаємо захоплення зображення до сигналу про завершення завантаження
    web.loadFinished.connect(capture)

    # Завантажуємо HTML-файл
    web.load(f'file:///{html_file}')

    # Запускаємо головний цикл додатка
    app.exec()




# Приклад виклику
html_file = 'SEND.html'
output_image = 'output_image.png'



def generation_image():
    render_html_to_image(html_file, output_image)
generation_image()
