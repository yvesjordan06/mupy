import os

import userdatamanager.utils as utils


class UserDataManager:
    def __init__(self):
        settings = utils.load_json("settings.json")
        self.base_dir = settings["base_dir"]
        self.original_dir = settings["original_dir"] if "original_dir" in settings else "original"
        self.results_dir = settings["results_dir"] if "results_dir" in settings else "results"
        self.testcases_dir = settings["testcases_dir"] if "testcases_dir" in settings else "testcases"
        self.create_base_dir()

    def create_base_dir(self):
        if not os.path.isdir(self.base_dir):
            os.mkdir(self.base_dir)

    def check_userdata(self, email):
        folder_name = utils.email_to_folder_name(email)
        folder_path = os.path.join(self.base_dir, folder_name)
        return os.path.isdir(folder_path)

    def get_original_path(self, email, name = None):
        folder_name = utils.email_to_folder_name(email)
        original_folder_path = os.path.join(self.base_dir, folder_name, self.original_dir)
        if name is None:
            return original_folder_path
        return os.path.join(original_folder_path, utils.get_file_name(name))

    def get_testcases_path(self, email, name = None):
        folder_name = utils.email_to_folder_name(email)
        testcases_folder_path = os.path.join(self.base_dir, folder_name, self.testcases_dir)
        if name is None:
            return testcases_folder_path
        return os.path.join(testcases_folder_path, utils.get_file_name(name))

    def get_results_path(self, email, name = None):
        folder_name = utils.email_to_folder_name(email)
        results_folder_path = os.path.join(self.base_dir, folder_name, self.results_dir)
        if name is None:
            return results_folder_path
        return os.path.join(results_folder_path, utils.get_file_name(name))



    def create_userdata(self, email):
        """
        This method creates a new user directory for the given email.

        It first converts the email into a valid folder name, then checks if a directory with that name already exists.
        If it does, an exception is raised. If it doesn't, a new directory is created with subdirectories for 'original', 'results', and 'testcases'.

        Args:
            email (str): The email of the user.

        Returns:
            str: The path to the newly created user directory.

        Raises:
            Exception: If a user directory with the given email already exists.
        """
        folder_name = utils.email_to_folder_name(email)
        if self.check_userdata(email):
            raise Exception("User already exists")
        folder_path = os.path.join(self.base_dir, folder_name)
        os.mkdir(folder_path)

        folders = [self.get_original_path(email), self.get_results_path(email), self.get_testcases_path(email)]
        for folder in folders:
            os.mkdir(folder)

        return folder_path

    def insert_original(self, email, code, name):
        """
        This method creates a Python file with the given name and code in the 'original' subdirectory of the user's directory.

        Args:
            email (str): The email of the user.
            code (str): The Python code to be written to the file.
            name (str): The name of the Python file.

        Raises:
            Exception: If the user's directory does not exist.
        """
        original_folder_path = self.get_original_path(email)

        if not os.path.isdir(original_folder_path):
            os.mkdir(original_folder_path)

        file_path = os.path.join(original_folder_path, utils.get_file_name(name))

        with open(file_path, 'w') as f:
            f.write(code)

    def insert_testcase(self, email, code, name):
        """
        This method creates a Python file with the given name and code in the 'testcases' subdirectory of the user's directory.

        Args:
            email (str): The email of the user.
            code (str): The Python code to be written to the file.
            name (str): The name of the Python file.

        Raises:
            Exception: If the user's directory does not exist.
        """

        testcases_folder_path = self.get_testcases_path(email)

        if not os.path.isdir(testcases_folder_path):
            os.mkdir(testcases_folder_path)

        file_path = os.path.join(testcases_folder_path, utils.get_file_name(name))

        with open(file_path, 'w') as f:
            f.write(code)


    def get_original_list(self, email):
        """
        This method returns a list of all Python files in the 'original' subdirectory of the user's directory.

        Args:
            email (str): The email of the user.

        Returns:
            list: A list of all Python files in the 'original' subdirectory of the user's directory.

        Raises:
            Exception: If the user's directory does not exist.
        """
        original_folder_path = self.get_original_path(email)

        if not os.path.isdir(original_folder_path):
            os.mkdir(original_folder_path)

        return os.listdir(original_folder_path)

    def get_testcase_list(self, email):
        """
        This method returns a list of all Python files in the 'testcases' subdirectory of the user's directory.

        Args:
            email (str): The email of the user.

        Returns:
            list: A list of all Python files in the 'testcases' subdirectory of the user's directory.

        Raises:
            Exception: If the user's directory does not exist.
        """
        testcases_folder_path = self.get_testcases_path(email)

        if not os.path.isdir(testcases_folder_path):
            os.mkdir(testcases_folder_path)

        return os.listdir(testcases_folder_path)

    def get_original(self, email, name):
        """
        This method returns the content of the Python file with the given name in the 'original' subdirectory of the user's directory.

        Args:
            email (str): The email of the user.
            name (str): The name of the Python file.

        Returns:
            str: The content of the Python file with the given name in the 'original' subdirectory of the user's directory.

        Raises:
            Exception: If the user's directory does not exist.
        """
        original_folder_path = self.get_original_path(email)

        if not os.path.isdir(original_folder_path):
            os.mkdir(original_folder_path)

        file_path = os.path.join(original_folder_path, utils.get_file_name(name))

        with open(file_path, 'r') as f:
            return f.read()

    def get_testcase(self, email, name):
        """
        This method returns the content of the Python file with the given name in the 'testcases' subdirectory of the user's directory.

        Args:
            email (str): The email of the user.
            name (str): The name of the Python file.

        Returns:
            str: The content of the Python file with the given name in the 'testcases' subdirectory of the user's directory.

        Raises:
            Exception: If the user's directory does not exist.
        """
        testcases_folder_path = self.get_testcases_path(email)

        if not os.path.isdir(testcases_folder_path):
            os.mkdir(testcases_folder_path)

        file_path = os.path.join(testcases_folder_path, utils.get_file_name(name))

        with open(file_path, 'r') as f:
            return f.read()