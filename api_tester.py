import fire
import requests

# NOTE: Adjust these settings as needed
API_HOST = "http://localhost:8000"
RESOURCE_URI = "profiles"
USERNAME = "admin"
PASSWORD = "admin"


class ApiTester:
    """CLI for testing API
    Server must be running.
    WARNING: Database queries are performed on supplied database.
        So be extra careful and/or use a test database.
    """

    def __init__(self, host=API_HOST):
        self.host = host

    def fetch_tokens(self):
        """Fetches access and refresh JWT tokens from api

        Returns:
            tuple: access,refresh
        """

        token_url = f"{self.host}/api/token/"

        response = requests.post(
            token_url, json={"username": USERNAME, "password": PASSWORD}
        )

        data = response.json()

        tokens = data["access"], data["refresh"]

        return tokens

    def get_all(self):
        """get list of all resources from api
        Usage: python api_tester.py get_all

        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/{RESOURCE_URI}/"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.get(url, headers=headers)

        return response.json() or 'No resources'

    def get_one(self, id):
        """get 1 resource by id from api

        Usage:
        python api_tester.py get_one 1

        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/{RESOURCE_URI}/{id}"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.get(url, headers=headers)

        return response.json()

    # TODO adjust parameter names to match API
    def create(self, owner, name, age, city, state, gender, partner_preferences, zodiac, description=None, hobbies_interests=None):
        """creates a resource in api

        Usage:
        python api_tester.py create /
            --owner=required --name=required 
            --age=required   --city=required
            --state=required --gender=required
            --partner_preferences = required
            --zodiac = required --description=optional
            --hobbies_interests=optional
        Returns: JSON
        """

        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/{RESOURCE_URI}/"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        data = {
            "name": name,
            "age": age,
            "gender": gender,
            "city": city,
            "state": state,
            "partner_preferences": partner_preferences,
            "description": description,
            "hobbies_interests": hobbies_interests,
            "zodiac": zodiac,
            "owner": owner,
        }

        response = requests.post(url, json=data, headers=headers)

        return response.json()

    def update(self, id, owner, name, age, city, state, gender, partner_preferences, zodiac, description=None, hobbies_interests=None):
        """updates a resource in api

        Usage:
        python api_tester.py update 1 /
            --owner=required --name=required 
            --age=required   --city=required
            --state=required --gender=required
            --partner_preferences = required
            --zodiac = required --description=optional
            --hobbies_interests=optional

        Returns: JSON
        """

        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/{RESOURCE_URI}/{id}/"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        original = self.get_one(id)

        data = {
            "name": name or original["name"],
            "age" : age or original["age"],
            "city": city or original["city"],
            "state": state or original["state"],
            "gender": gender or original["gender"],
            "partner_preferences": partner_preferences or original["partner_preferences"],
            "description": description or original["description"],
            "zodiac": zodiac or original["zodiac"],
            "hobbies_interests": hobbies_interests or original["hobbies_interests"],
            "owner": owner or original["owner"],
        }

        response = requests.put(url, json=data, headers=headers)

        return response.text

    def delete(self, id):
        """deletes a resource in api

        Usage:
        python api_tester.py delete 1

        Returns: Empty string if no error
        """

        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/{RESOURCE_URI}/{id}/"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.delete(url, headers=headers)

        return response.text


if __name__ == "__main__":
    fire.Fire(ApiTester)
