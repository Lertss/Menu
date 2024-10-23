import os
import shutil
import tempfile
import unittest

from service.service import create_folders


class TestCreateFolders(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        # Save the original working directory
        self.original_cwd = os.getcwd()
        # Change the working directory to a temporary one
        os.chdir(self.test_dir)

    def tearDown(self):
        # Return to the original working directory
        os.chdir(self.original_cwd)
        # Delete a temporary directory
        shutil.rmtree(self.test_dir)

    def test_create_folders(self):
        # Calling a function to create folders
        create_folders()

        # Folder names
        base_folder_name = "Folder"
        screenshot_folder_name = "screenshot"
        sub_folder_name_image_back = "image_background"
        sub_folder_name_zdjecia = "Zdjęcia"

        # Expected paths
        base_folder_path = os.path.join(self.test_dir, base_folder_name)
        sub_folder_path_screenshot = os.path.join(base_folder_path, screenshot_folder_name)
        sub_folder_path_image_back = os.path.join(base_folder_path, sub_folder_name_image_back)
        sub_folder_path_image_zdjecia = os.path.join(self.test_dir, sub_folder_name_zdjecia)

        # Check the existence of the main folder
        self.assertTrue(os.path.isdir(base_folder_path), "The main folder was not created")

        # Check for the existence of subfolders
        self.assertTrue(os.path.isdir(sub_folder_path_screenshot), "The 'screenshot' subfolder was not created")
        self.assertTrue(os.path.isdir(sub_folder_path_image_back), "The 'image_background' subfolder was not created")
        self.assertTrue(os.path.isdir(sub_folder_path_image_zdjecia), "The 'Zdjęcia' subfolder was not created in the correct location")

        # Additional check if the 'Zdjęcia' folder is created in the main folder
        incorrect_sub_folder_path_image_zdjecia = os.path.join(base_folder_path, sub_folder_name_zdjecia)
        self.assertFalse(os.path.exists(incorrect_sub_folder_path_image_zdjecia), "The 'Zdjęcia' subfolder was created in the wrong location")
