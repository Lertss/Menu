import logging
import os


def create_folders():
    """Create folders and subfolders"""
    # Name of the main folder
    base_folder_name = "Folder"
    # Name of the folders to be created inside the main folder
    sub_folder_name_html = "HTML"
    sub_folder_name_log_bd = "LOG"
    sub_folder_name_image_back = "image_background"
    sub_folder_name_zdjecia = "Zdjęcia"
    # The path to the main folder
    base_folder_path = os.path.join(os.getcwd(), base_folder_name)
    # Check the existence of the main folder
    if not os.path.exists(base_folder_path):
        # Create a main folder if it does not exist
        os.makedirs(base_folder_path)
        logging.info(f"Folder '{base_folder_name}' został utworzony.")
    else:
        logging.warning(f"Folder '{base_folder_name}' już istnieje.")

    # Path to a subfolder within the main folder
    sub_folder_path_html = os.path.join(base_folder_path, sub_folder_name_html)
    sub_folder_path_log_bd = os.path.join(base_folder_path, sub_folder_name_log_bd)
    sub_folder_path_image_back = os.path.join(base_folder_path, sub_folder_name_image_back)
    sub_folder_path_image_zdjecia = os.path.join(base_folder_path, sub_folder_name_html)
    # Check the existence of a subfolder
    if not os.path.exists(sub_folder_path_html):
        # Create a subfolder if it does not exist
        os.makedirs(sub_folder_path_html)
        logging.info(f"Folder '{sub_folder_name_html}' został utworzony w folderze {base_folder_name}.")
    else:
        logging.warning(f"Folder '{sub_folder_name_html}' już istnieje w folderze {base_folder_name}.")

    if not os.path.exists(sub_folder_path_log_bd):
        os.makedirs(sub_folder_path_log_bd)
        logging.info(f"Folder '{sub_folder_name_log_bd}' został utworzony w folderze {base_folder_name}.")
    else:
        logging.warning(f"Folder '{sub_folder_name_log_bd}' już istnieje w folderze {base_folder_name}.")

    if not os.path.exists(sub_folder_path_image_back):
        os.makedirs(sub_folder_path_image_back)
        logging.info(f"Folder '{sub_folder_name_image_back}' został utworzony w folderze {base_folder_name}.")
    else:
        logging.warning(f"Folder '{sub_folder_name_image_back}' już istnieje w folderze {base_folder_name}.")

    if not os.path.exists(sub_folder_path_image_zdjecia):
        os.makedirs(sub_folder_path_image_zdjecia)
        logging.info(f"Folder '{sub_folder_name_zdjecia}' został utworzony w folderze {base_folder_name}.")
    else:
        logging.warning(f"Folder '{sub_folder_name_zdjecia}' już istnieje w folderze {base_folder_name}.")


def create_log_file():
    log_folder = "Folder/LOG"
    log_file_path = os.path.join(log_folder, "app.log")

    # Перевірка, чи папка і файл існують
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)  # Створення папки, якщо її немає

    if not os.path.exists(log_file_path):
        with open(log_file_path, 'w') as f:
            f.write("")  # Створення порожнього файлу, якщо його немає


MAX_LOGS = 500


def trim_log_file():
    """limit of 500 entries in the log"""
    try:
        with open('app.log', 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Saving the last MAX_LOGS lines
        lines = lines[-MAX_LOGS:]

        with open('app.log', 'w', encoding='utf-8') as f:
            f.writelines(lines)
    except FileNotFoundError:
        # If the file does not exist, do nothing
        pass