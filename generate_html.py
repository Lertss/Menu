import logging
from models.case import Case
from models.case_state import CaseState, Category
from models.database import Session
from models.database_worker import Worker
from PySide6.QtWidgets import QMessageBox
from playwright.sync_api import sync_playwright
import subprocess
from PIL import Image
import os

current_directory = os.getcwd()


def save_html(html_content, file_path):
    try:
        with open(file_path, "w", encoding="utf-8") as html_file:
            html_file.write(html_content)
        return True
    except FileNotFoundError as e:
        error_message = f"File not found: {file_path}. *save_html"
        logging.error(error_message)
        QMessageBox.critical(None, "Error", error_message)
        return False
    except IOError as e:
        error_message = f"Error writing to file: {file_path}. *save_html"
        logging.error(error_message)
        QMessageBox.critical(None, "Error", error_message)
        return False


def initialize_session():
    session = Session()
    categories = session.query(Category).all()
    session.close()
    return session, categories


def generate_html_with_list_druk(worker, state_id):
    categories = worker.getCategories()
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

            .container div:nth-child(2) {
                border-bottom: 3px dotted;
                height: 1px;
            }

            .text-eng{
                font-size: 45px;
                font-weight: lighter;
            }
            div{
                font-weight: bold;
            }

            body {
                font-size: 45px;
                margin: 0; 
                padding: 0; 
                margin-right: 25px;
                
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
        cases = session.query(Case).filter(Case.category == category.id, Case.case_state == 1).all()
        typ_pomiaru = category.pomiar
        session.close()
        # Check for cases in the category
        if cases:
            html_content += f"""
                    <li>
                        <h3>{category.category_name}</h3>
                        <ul>

            """
            for item in cases:
                html_content += f"""
                            <li>
                                <div class="container">
                                    <div style="text-align: left;" class="name">-{item.name}</div>
                                    <div></div>
                                    <div style="text-align: right;">
                                        <span class="text-eng masa blue">({item.masa} {typ_pomiaru})</span>
                                        <span class="price blue">{item.price} zł</span>
                                    </div>
                                </div>
                            </li>
                            <li>
                                <div class="text-eng description">
                                    ({item.description})<br>
                                    {item.description_english}
                                </div>
                            </li>
                """
            html_content += """
                        </ul>
                    </li>
            """

    html_content += """
                </ul>
            </section>
        </main>
    </div>
    </body>
    </html>
    """

    return html_content


def generate_html_with_list_send(worker, state_id):
    categories = worker.getCategories()
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
                                margin-top: -50px
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

            .container div:nth-child(2) {
                border-bottom: 3px dotted;
                height: 1px;
            }

            .text-eng{
                font-size: 45px;
                font-weight: lighter;
            }
            div{
                font-weight: bold;
            }

            body{
                font-size: 45px;
                margin: 0; 
                padding: 0; 
                margin-right: 25px;
                width: 1450px;
                color: rgb(130, 174, 90);
                background-image: url('../image_background/tlo.jpeg');
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-size: 1500px 100vh;
                min-height: 100vh;
                background-position: top left;
                overflow: hidden;
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
                color: rgb(255, 126, 40);
            }

            .blue {
                color: yellow;
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
        cases = session.query(Case).filter(Case.category == category.id, Case.case_state == 1).all()
        typ_pomiaru = category.pomiar
        session.close()
        # Check for cases in the category
        if cases:
            html_content += f"""
                    <li>
                        <h3>{category.category_name}</h3>
                        <ul>

            """
            for item in cases:
                html_content += f"""
                            <li>
                                <div class="container">
                                    <div style="text-align: left;" class="name">-{item.name}</div>
                                    <div></div>
                                    <div style="text-align: right;">
                                        <span class="text-eng masa blue">({item.masa} {typ_pomiaru})</span>
                                        <span class="price blue">{item.price} zł</span>
                                    </div>
                                </div>
                            </li>
                            <li>
                                <div class="text-eng description">
                                    ({item.description})<br>
                                    {item.description_english}
                                </div>
                            </li>
                """
            html_content += """
                        </ul>
                    </li>
            """

    html_content += """
                </ul>
            </section>
        </main>
    </div>
    </body>
    </html>
    """

    return html_content


html_directory = os.path.join(current_directory, "Folder", "HTML")
image_directory = os.path.join(current_directory, "Folder", "Zdjęcia")


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

    if save_html(html_content_druk, file_path_druk):
        logging.info(f"html generated and saved at {file_path_druk}. *create_pdf")
    else:
        logging.info("Failed to generate html druk. *create_pdf")
    if save_html(html_content_send, file_path_send):
        logging.info(f"html generated and saved at {file_path_send}. *create_pdf")
        create_image()
    else:
        logging.info("Failed to generate html send. *create_pdf")







def create_image():
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe")
        page_send = browser.new_page()
        page_druk = browser.new_page()

        logging.info(browser)
        logging.info(page_send)
        logging.info(page_druk)

        page_send.goto(rf'{html_directory}/SEND.html')
        page_druk.goto(rf'{html_directory}/DRUK.html')

        # Get the full height of the page
        full_height_send = page_send.evaluate("() => document.body.scrollHeight")
        full_height_druk = page_druk.evaluate("() => document.body.scrollHeight")

        # Set the viewport to the full height of the page
        page_send.set_viewport_size({"width": 1500, "height": full_height_send})
        page_druk.set_viewport_size({"width": 1050, "height": full_height_druk})

        page_send.screenshot(path=rf'{image_directory}/SEND_full.png', full_page=True)
        page_druk.screenshot(path=rf'{image_directory}/DRUK_full.png', full_page=True)

        # Open the full screenshots
        send_full_image = Image.open(rf'{image_directory}/SEND_full.png')
        druk_full_image = Image.open(rf'{image_directory}/DRUK_full.png')

        # Crop 15px from the bottom
        send_cropped_image = send_full_image.crop((0, 0, send_full_image.width, send_full_image.height - 15))
        druk_cropped_image = druk_full_image.crop((0, 0, druk_full_image.width, druk_full_image.height - 15))

        # Save the cropped images
        send_cropped_image.save(rf'{image_directory}/SEND.png')
        druk_cropped_image.save(rf'{image_directory}/DRUK.png')

        # Close the browser
        browser.close()
    try:
        subprocess.run(
            [r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe', rf'{html_directory}/DRUK.html'])
    except FileNotFoundError as e:
        logging.error(f"Error opening DRUK.html: {e} *create_image")
