import requests
from dotenv import load_dotenv
import os

DEFAULT_WEIGHT = 90
DEFAULT_HEIGHT = 192
DEFAULT_AGE = 28

"""
The Nutrition & Exercise API is used for natural language processing of user input and conversion into exercise data.
Estimations are made for duration and calories burned based on the parameters defined in the user.
"""


# load open nutritionix environment parameters
load_dotenv(".env")
# nutritionix parameters
app_id = os.getenv("app_id")
app_key = os.getenv("app_key")


def query_exercise_from_user():
    return input("Tell me what exercise you did: ")


class NutritionixUser:

    def __init__(self, weight=DEFAULT_WEIGHT, height=DEFAULT_HEIGHT, age=DEFAULT_AGE, app_id=app_id, app_key=app_key):
        self.weight = weight
        self.height = height
        self.age = age
        self.app_id = app_id
        self.app_key = app_key

    def get_nutritionix_response(self):
        headers = {
            'Content-Type': 'application/json',
            'x-app-id': self.app_id,
            'x-app-key': self.app_key
        }

        params = {
            "query": query_exercise_from_user(),
            "weight_kg": self.weight,
            "height_cm": self.height,
            "age": self.age
        }

        response = requests.post(
            url='https://trackapi.nutritionix.com/v2/natural/exercise',
            json=params,
            headers=headers
        )
        return response.json()["exercises"]
