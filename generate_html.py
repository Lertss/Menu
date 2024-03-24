from io import BytesIO

from xhtml2pdf import pisa
from xhtml2pdf.files import pisaFileObject

from models.case_state import CaseState
from models.database import Session
from models.database_worker import Worker


def save_html(html_content, file_path):
    with open(file_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)


# Пример использования


def generate_html_with_list(worker, state_id):
    state = worker.session.query(CaseState).filter_by(id=state_id).first()
    cases = worker.getCases(state)

    html_content = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dziś polecamy</title>
    <style>
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
            margin-right: 40px;
        }
        h1{
            text-align: center;
        }
        
        h3{
            margin-left: 100px;
            font-size: 35px;
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
                <li>
                    <h3>Zupy</h3>
                    <ul>
                        """

    for item in cases:
        if item.category == 1:
            html_content += f"""
                        <li>
                            <div class="container">
                                <div style="text-align: left;">{item.name} <span class="text-eng">({item.masa} ml)</span></div>
                                <div></div>
                                <div style="text-align: right;"><span>{item.price} zł</span></div>
                            </div>
                        </li>

                        <li>
                            <div class="text-eng">
                                ({item.name_eng})
                            </div>
                        </li>
                        """
    html_content += f"""
                    </ul>
                </li>
                <li>
                    <h3>Вторые блюда</h3>
<ul>
                        """

    for item in cases:
        if item.category == 1:
            html_content += f"""
                        <li>
                            <div class="container">
                                <div style="text-align: left;">{item.name} <span class="text-eng">({item.masa} ml)</span></div>
                                <div></div>
                                <div style="text-align: right;"><span>{item.price} zł</span></div>
                            </div>
                        </li>

                        <li>
                            <div class="text-eng">
                                ({item.name_eng})
                            </div>
                        </li>
                        """
    html_content += f"""
                    </ul>
                </li>
                <li>
                    <h3>Напитки</h3>
                    <ul>
                        <li><span>Горячая шоколад</span> - 11 zł</li>
                        <li><span>с вишневкой</span> - 14 zł</li>
                    </ul>
                </li>
            </ul>
        </section>
    </main>
</div>
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
    file_path = "example.html"
    if save_html(html_content, file_path):
        print(f"html generated and saved at {file_path}")
    else:
        print("Failed to generate html.")


if __name__ == "__main__":
    generation_pdf()
