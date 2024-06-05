import json
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


    # Path to a subfolder within the main folder
    sub_folder_path_html = os.path.join(base_folder_path, sub_folder_name_html)
    sub_folder_path_log_bd = os.path.join(base_folder_path, sub_folder_name_log_bd)
    sub_folder_path_image_back = os.path.join(base_folder_path, sub_folder_name_image_back)
    sub_folder_path_image_zdjecia = os.path.join(base_folder_path, sub_folder_name_zdjecia)
    # Check the existence of a subfolder
    if not os.path.exists(sub_folder_path_html):
        # Create a subfolder if it does not exist
        os.makedirs(sub_folder_path_html)

    if not os.path.exists(sub_folder_path_log_bd):
        os.makedirs(sub_folder_path_log_bd)

    if not os.path.exists(sub_folder_path_image_back):
        os.makedirs(sub_folder_path_image_back)

    if not os.path.exists(sub_folder_path_image_zdjecia):
        os.makedirs(sub_folder_path_image_zdjecia)


def load_settings():
    if os.path.exists("Folder/LOG/settings.json"):
        with open("Folder/LOG/settings.json", "r") as file:
            return json.load(file)
    else:
        return {
            "headline": "rgb(130, 174, 90);",
            "category": "rgb(255, 126, 40)",
            "main": "rgb(130, 174, 90);",
            "masa": "yellow",
            "cena": "yellow",
            "english_dish": "rgb(130, 174, 90);",
            "description": "rgb(130, 174, 90);",
            "dodatki": "red"
        }


def save_settings(settings):
    with open("Folder/LOG/settings.json", "w") as file:
        json.dump(settings, file)
