import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """Send a GET request to the URL and return the response body."""
        response = requests.get(self.url)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        return response.content

    def load_json(self):
        """Use get_response_body to get the response, and convert it to a Python object."""
        response_body = self.get_response_body()
        return json.loads(response_body)  # Convert JSON string to Python dictionary/list