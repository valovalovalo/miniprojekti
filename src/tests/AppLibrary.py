import requests

class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5001"

    def setup_database(self):
        print("Setting up application")
        requests.get(f"{self._base_url}/setup_db")

    def reset_database(self):
        print("Resetting application")
        requests.get(f"{self._base_url}/reset_db")