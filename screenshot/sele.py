
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import tempfile




def take_full_screenshot_from_html(html_content, screenshot_output_path):
    """Function to create a temporary HTML file and take a screenshot"""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as temp_html:
        temp_html.write(html_content.encode('utf-8'))
        temp_html_path = temp_html.name

    chrome_options = Options()
    chrome_options.add_argument("--headless=old")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--no-sandbox")

    service = Service('C:/Users/sergz/PycharmProjects/Menu/chromedriver-win64/chromedriver.exe')  # Вкажіть шлях до ChromeDriver

    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(f"file://{temp_html_path}")

    height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(1500, height + 300)

    driver.save_screenshot(screenshot_output_path)

    driver.quit()


