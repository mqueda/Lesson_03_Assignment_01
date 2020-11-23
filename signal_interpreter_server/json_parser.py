"""
Module for implementing the json parser
"""
import json


class LoadAndParse:
    """
    Class for the LoadAndParse functionalities.
    """
    def __init__(self):
        """
        Sets the init values
        """
        self.data = None
        self.title = None

    def load_file(self, path):
        """
        Action : Load the specified json file.
        Expected Results : Proper file load.
        Returns: N/A.
        """
        with open(path, "r") as json_file:
            self.data = json.load(json_file)

    def return_signal_by_title(self, reqid):
        """
        Action : Return the service according with json file.
        Expected Results : Return the correct service.
        Returns: self.title.
        """
        services = self.data['services']
        for service in services:
            if service['id'] == reqid:
                self.title = service['title']
                print(self.title)
                return self.title
        return "Service not found!"
