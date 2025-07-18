import requests
from urllib.parse import urljoin


class BaseApiMethods:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_user(self, user_data):
        endpoint = urljoin(self.base_url, "user")
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        response = requests.post(endpoint, headers=headers, json=user_data)
        return response

    def get_user_by_user_name(self, user_name):
        endpoint = urljoin(self.base_url, "user/%s" %user_name)
        response = requests.get(endpoint)
        return response

    def update_user(self, user_data, user_name):
        endpoint = urljoin(self.base_url, "user/%s" %user_name)
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        response = requests.put(endpoint, headers=headers, json=user_data)
        return response

    def delete_user_by_user_name(self, user_name):
        endpoint = urljoin(self.base_url, "user/%s" %user_name)
        response = requests.delete(endpoint)
        return response

    def create_pet(self, pet_data):
        endpoint = urljoin(self.base_url, "pet")
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        response = requests.post(endpoint, headers=headers, json=pet_data)
        return response

    def get_pet_by_id(self, pet_id):
        endpoint = urljoin(self.base_url, f"pet/{pet_id}")
        response = requests.get(endpoint)
        return response

    def update_pet(self, pet_data):
        endpoint = urljoin(self.base_url, "pet")
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        response = requests.put(endpoint, headers=headers, json=pet_data)
        return response

    def delete_pet(self, pet_id):
        endpoint = urljoin(self.base_url, f"pet/{pet_id}")
        response = requests.delete(endpoint)
        return response
