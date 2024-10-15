import os


def create_folders():
    """Create folders and subfolders"""
    # Name of the main folder
    base_folder_name = "Folder"
    screenshot_folder_name = "screenshot"
    sub_folder_name_image_back = "image_background"
    sub_folder_name_zdjecia = "Zdjęcia"
    # The path to the main folder
    base_folder_path = os.path.join(os.getcwd(), base_folder_name)
    # Check the existence of the main folder
    if not os.path.exists(base_folder_path):
        # Create a main folder if it does not exist
        os.makedirs(base_folder_path)

    # Path to a subfolder within the main folder
    sub_folder_path_screenshot = os.path.join(
        base_folder_path, screenshot_folder_name
    )
    sub_folder_path_image_back = os.path.join(
        base_folder_path, sub_folder_name_image_back
    )
    sub_folder_path_image_zdjecia = os.path.join(
        sub_folder_name_zdjecia
    )

    if not os.path.exists(sub_folder_path_screenshot):
        os.makedirs(sub_folder_path_screenshot)

    if not os.path.exists(sub_folder_path_image_back):
        os.makedirs(sub_folder_path_image_back)

    if not os.path.exists(sub_folder_path_image_zdjecia):
        os.makedirs(sub_folder_path_image_zdjecia)



