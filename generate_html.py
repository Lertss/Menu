from playwright.sync_api import sync_playwright
from models.case_state import Category
from models.database import Session
from models.database_worker import Worker


def save_html(html_content, file_path):
    with open(file_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)


def generate_html_with_list(worker, state_id):
    categories = worker.getCategories()
    html_content = """
    <!DOCTYPE html>
    <html lang="ru">
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
            }
            li {
                list-style-type: none;
            }

            .container div:nth-child(2) {
                border-bottom: 3px dotted;
                height: 1px;
            }

            .text-eng{
                font-size: 22px;
                font-weight: lighter;
            }
            div{
                font-weight: bold;
            }

            body {
                font-size: 25px;
                margin: 0;
                padding: 0;
                margin-right: 25px;
            }
            h1{
                text-align: center;
                margin: 0;
            }

            h3{
                margin-left: 50px;
                font-size: 35px;
                margin-top: 10px;
                margin-bottom: 0;
            }
        </style>
    </head>
    <body>

    </body>
    </html>
    """

    return html_content


def generation_pdf():
    session = Session()
    worker = Worker(session)
    state_id = 1
    # Generate HTML content with the list
    html_content = generate_html_with_list(worker, state_id)
    session.close()
    file_path = "examples.html"
    if save_html(html_content, file_path):
        print(f"html generated and saved at {file_path}")
    else:
        print("Failed to generate html.")


def crete_image():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto(r'C:/Users/sergz/Desktop/Menu/examples.html')
        page.screenshot(path="screenshot.png", full_page=True)

        browser.close()


if __name__ == "__main__":
    generation_pdf()





