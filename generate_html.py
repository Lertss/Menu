from pathlib import Path

from PySide6.QtWidgets import QMessageBox, QApplication

from models.database import Session
from models.database_worker import getCategories, getDodatki, getColor
from models.dish import Dish
from screenshot.sele import take_full_screenshot_from_html


def generate_html_with_list(colore_bool):
    global color_str
    categories = getCategories()
    dodatki_list = getDodatki()

    if colore_bool:
        color_str = getColor()
        current_directory = Path.cwd()
        old_path = str(current_directory) + '/Folder/image_background/tlo.jpg'
        new_path = old_path.replace("\\", "/")
    else:
        new_path = None
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
                color: {color_str.dodatki if colore_bool else 'red'};
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
                color: {color_str.english_dish if colore_bool else 'black'};
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
                color: {color_str.main if colore_bool else 'black'};
                background-image: url('{new_path}');
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
                color: {color_str.headline if colore_bool else 'black'};
            }}

            h3{{
                margin-left: 100px;
                font-size: 60px;
                margin-top: 10px;
                margin-bottom: 0;
                color: {color_str.category if colore_bool else 'black'};
            }}

            .masa {{
                color: {color_str.masa if colore_bool else 'black'};
            }}
            .cena {{
                color: {color_str.cena if colore_bool else 'black'};
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
        with Session() as session:
            dishs = (
                session.query(Dish)
                .filter(Dish.category == category.id, Dish.dish_state == 1)
                .all()
            )

            typ_pomiaru = category.pomiar

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
                                             <span style="color: {color_str.description if colore_bool else 'black'};">
                                                ({item.description})<br>
                                               </span>
                                                <span style="color: {color_str.english_dish if colore_bool else 'black'};">
                                                    {item.description_english}
                                                </span>
                                            </div>
                                        </li>
                                """
                else:
                    html_content += f"""
                            <li>
                                <div class="text-eng description">
                                <span style="color: {color_str.english_dish if colore_bool else 'black'};">
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
              </section>
            </main>
            </div>
            <div class="dodatki">
                    <p>
                        {dodatki.text if dodatki else ""}
                        <br>
                        <br>
                        <span>
                        {dodatki.text_eng if dodatki else ""}
                        </span>
                    </p>
                </div>

    </body>
    </html>
    """

    return html_content


def generation_pdf():
    try:
        create_image()
    except Exception as e:
        msgbox = QMessageBox()
        msgbox.setText("Bląd:")
        msgbox.setInformativeText(
            f"Wystąpił błąd podczas tworzenia obrazów - {e}"
        )
        msgbox.exec()


def create_image():
    current_directory = Path.cwd()
    for i in [['SEND', True], ['DRUK', False]]:
        old_path = str(current_directory) + f'/Zdjęcia/{i[0]}.png'
        new_path = old_path.replace("\\", "/")

        take_full_screenshot_from_html(generate_html_with_list(i[1]), new_path)
    QApplication.quit()
