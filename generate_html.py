import os

from playwright.sync_api import sync_playwright
from PySide6.QtWidgets import QMessageBox

from models.database import Session
from models.database_worker import Worker
from models.dish import Dish
from models.dish_state import Category
from service.service import load_settings

current_directory = os.getcwd()


def save_html(html_content, file_path):
    try:
        with open(file_path, "w", encoding="utf-8") as html_file:
            html_file.write(html_content)
        return True
    except FileNotFoundError:
        error_message = f"File not found: {file_path}. *save_html"
        QMessageBox.critical(None, "Error", error_message)
        return False
    except IOError:
        error_message = f"Error writing to file: {file_path}. *save_html"
        QMessageBox.critical(None, "Error", error_message)
        return False


def initialize_session():
    session = Session()
    categories = session.query(Category).order_by(Category.turn_number).all()
    session.close()
    return session, categories


def generate_html_with_list_druk(worker, state_id):
    categories = worker.getCategories()
    dodatki_list = worker.getDodatki()
    if dodatki_list:
        dodatki = dodatki_list[0]
    else:
        dodatki = None

    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dziś polecamy</title>
        <style>
            .a4-container {
                margin-left: -40px;
            }
            .container {
                display: grid;
                grid-template-columns: auto 1fr auto;
                align-items: end;
                margin-top: 10px
            }
            li {
                list-style-type: none;
            }
            .category_eng{
            font-weight:100;
            }
            .container div:nth-child(2) {
                border-bottom: 3px dotted;
                height: 1px;
            }
            .text-eng{
                font-size: 45px;
                font-weight: lighter;
            }
            .dodatki {
                font-weight: normal;
                color: red;
                margin-left: 40px;
                margin-right: 40px;
            }


            div{
                font-weight: bold;
            }

            body {
                font-size: 45px;
                margin: 0;
                padding: 0;
                width: 1450px;
                margin-right: 100px;

            }
            h1{
                text-align: center;
                margin: 15px;
            }

            h3{
                margin-left: 100px;
                font-size: 60px;
                margin-top: 10px;
                margin-bottom: 0;
            }
        </style>
    </head>
    <body>
    <div class="a4-container">
        <header>
            <h1>Dziś polecamy</h1>
        </header>
        <main>
            <section class="menu">
                <ul>
    """

    for category in categories:
        session, categories = initialize_session()
        dishs = (
            session.query(Dish)
            .filter(Dish.category == category.id, Dish.dish_state == 1)
            .all()
        )
        typ_pomiaru = category.pomiar
        session.close()
        # Check for dishs in the category
        if dishs:
            html_content += f"""
    <li>
        <h3>{category.category_name} <span class="category_eng">({category.category_eng_name})</span></h3>
        <ul>

                        """
            for item in dishs:
                html_content += f"""
                                        <li>
                                            <div class="container">
                                                <div style="text-align: left;" class="name">-{item.name}</div>
                                                <div></div>
                                                <div style="text-align: right;">
                            """
                if item.masa and typ_pomiaru:  #
                    html_content += f"""
                                                    <span class="text-eng masa blue">({item.masa} {typ_pomiaru})</span>
                                """
                html_content += f"""
                                                    <span class="price blue">{item.price} zł</span>
                                                </div>
                                            </div>
                                        </li>
                            """
                if item.description:  # Check if the description exists
                    html_content += f"""
                                        <li>
                                            <div class="text-eng description">
                                                ({item.description})<br>
                                                {item.description_english}
                                            </div>
                                        </li>
                                """
                else:
                    html_content += f"""
                            <li>
                                <div class="text-eng description">
                                    {item.description_english}
                                </div>
                            </li>

                    """

            html_content += """
                        </ul>
                    </li>
            """

    html_content += f"""

                </ul>
            </main>
            </div>
            <div class="dodatki">
                    <p >
                        {dodatki.text if dodatki else ""}
                        <br>
                        <br>
                        {dodatki.text_eng if dodatki else ""}
                    </p>
                </div>
        </section>
    </body>
    </html>
    """

    return html_content


def generate_html_with_list_send(worker, state_id):
    settings = load_settings()
    categories = worker.getCategories()
    dodatki_list = worker.getDodatki()
    if dodatki_list:
        dodatki = dodatki_list[0]
    else:
        dodatki = None

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dziś polecamy</title>
        <style>
            .a4-container {{
                margin-left: -40px;
                margin-top: -50px
            }}
            .container {{
                display: grid;
                grid-template-columns: auto 1fr auto;
                align-items: end;
                margin-top: 10px
            }}
            li {{
                list-style-type: none;
            }}
             .dodatki {{
                font-weight: normal;
                color: {settings['dodatki']};
                margin-left: 40px;
                margin-right: 40px;
            }}
            .container div:nth-child(2) {{
                border-bottom: 3px dotted;
                height: 1px;
            }}

            .text-eng{{
                font-size: 45px;
                font-weight: lighter;
                color: {settings['english_dish']};
            }}
            div{{
                font-weight: bold;
            }}

            body{{
                font-size: 45px;
                margin: 0;
                padding: 0;
                margin-right: 25px;
                width: 1450px;
                color: {settings['main']};
                background-image: url('../image_background/tlo.jpeg');
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-size: 1500px 120vh;
                min-height: 100vh;
                background-position: top left;
                overflow: hidden;
                margin-bottom: 150px;
            }}
             .category_eng{{
            font-weight:100;
            }}
            h1{{
                text-align: center;
                margin: 15px;
                margin-top: 125px;
                color: {settings['headline']};
            }}

            h3{{
                margin-left: 100px;
                font-size: 60px;
                margin-top: 10px;
                margin-bottom: 0;
                color: {settings['category']};
            }}

            .masa {{
                color: {settings['masa']};
            }}
            .cena {{
                color: {settings['cena']};
            }}
        </style>
    </head>
    <body>
    <div class="a4-container">
        <header>
            <h1>Dziś polecamy</h1>
        </header>
        <main>
            <section class="menu">
                <ul>
    """

    for category in categories:
        session, categories = initialize_session()
        dishs = (
            session.query(Dish)
            .filter(Dish.category == category.id, Dish.dish_state == 1)
            .all()
        )
        typ_pomiaru = category.pomiar
        session.close()
        # Check for dishs in the category
        if dishs:
            html_content += f"""
                                <li>
        <h3>{category.category_name} <span class="category_eng">({category.category_eng_name})</span></h3>
        <ul>
                        """
            for item in dishs:
                html_content += f"""
                                        <li>
                                            <div class="container">
                                                <div style="text-align: left;" class="name">-{item.name}</div>
                                                <div></div>
                                                <div style="text-align: right;">
                            """
                if (
                    item.masa and typ_pomiaru
                ):  # Check if item.masa and typ_pomiaru are not empty
                    html_content += f"""
                                                    <span class="text-eng masa">({item.masa} {typ_pomiaru})</span>
                                """
                html_content += f"""
                                                    <span class="cena">{item.price} zł</span>
                                                </div>
                                            </div>
                                        </li>
                            """
                if item.description:
                    html_content += f"""
                                        <li>
                                            <div class="text-eng description">
                                             <span style="color: {settings['description']};">
                                                ({item.description})<br>
                                               </span>
                                                <span style="color: {settings['english_dish']};">
                                                    {item.description_english}
                                                </span>
                                            </div>
                                        </li>
                                """
                else:
                    html_content += f"""
                            <li>
                                <div class="text-eng description">
                                <span style="color: {settings['english_dish']};">
                                    {item.description_english}
                                </span>
                                </div>
                            </li>

                    """

            html_content += """
                        </ul>
                    </li>
            """

    html_content += f"""

                </ul>
            </main>
            </div>
            <div class="dodatki">
                    <p>
                        {dodatki.text if dodatki else ""}
                        <br>
                        <br>
                        <span style="color: {settings['english_dish']};">
                        {dodatki.text_eng if dodatki else ""}
                        </span>
                    </p>
                </div>
        </section>
    </body>
    </html>
    """

    return html_content


html_directory = os.path.join(current_directory, "Folder", "HTML")
image_directory = os.path.join(current_directory, "Zdjęcia")


def generation_pdf():
    session = Session()
    worker = Worker(session)
    state_id = 1
    # Generate HTML content with the list
    html_content_druk = generate_html_with_list_druk(worker, state_id)
    html_content_send = generate_html_with_list_send(worker, state_id)

    # Ensure HTML directory exists
    if not os.path.exists(html_directory):
        os.makedirs(html_directory)

    file_path_druk = os.path.join(html_directory, "DRUK.html")
    file_path_send = os.path.join(html_directory, "SEND.html")

    if save_html(html_content_druk, file_path_druk) and save_html(
        html_content_send, file_path_send
    ):
        create_image()
    else:
        msgbox = QMessageBox()
        msgbox.setText("Bląd:")
        msgbox.setInformativeText(
            "Wystąpił błąd podczas tworzenia plików html i obrazów."
        )
        msgbox.exec()


def find_file(filename, search_path):
    result = []

    # Search all files and folders in the specified directory
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))

    return result


# Look for chrome.exe in the Program Files and Program Files (x86) directories
chrome_files = find_file("chrome.exe", "C:\\Program Files")
chrome_files += find_file("chrome.exe", "C:\\Program Files (x86)")


def create_image():
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chrome_files[0])
        try:
            page_send = browser.new_page()
            page_druk = browser.new_page()

            page_send.goto(rf"{html_directory}/SEND.html")
            page_druk.goto(rf"{html_directory}/DRUK.html")
            # Get the full height of the page
            full_height_send = page_send.evaluate("() => document.body.scrollHeight")
            full_height_druk = page_druk.evaluate("() => document.body.scrollHeight")
            # Set the viewport to the full height of the page
            page_send.set_viewport_size({"width": 1500, "height": full_height_send})
            page_druk.set_viewport_size({"width": 1500, "height": full_height_druk})

            page_send.screenshot(path=rf"{image_directory}/SEND.png", full_page=True)
            page_druk.screenshot(path=rf"{image_directory}/DRUK.png", full_page=True)
        finally:
            browser.close()
