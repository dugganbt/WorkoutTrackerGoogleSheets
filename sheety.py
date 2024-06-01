import requests
from dotenv import load_dotenv
import os
from datetime import datetime

"""
Sheety API is used to log exercise information extracted using Nutritionix API. For now the program only allows addition
of rows to the sheet, but no alteration. It also requires the sheet to be created in advance, and uses 1 defined sheet. 
"""

# load sheety api variables
load_dotenv(".env")
api_username = os.getenv("sheety_user")
api_projectname = os.getenv("sheety_projectname")
api_sheetname = os.getenv("sheety_sheetname")
api_token = os.getenv("sheety_token")

# create api endpoint
api_endpoint = f"https://api.sheety.co/{api_username}/{api_projectname}/{api_sheetname}"


def log_exercises(nutritionix_exercise_json_output):
    for exercise in nutritionix_exercise_json_output:

        print(f"Exercise: {exercise["name"]}, time spent: {exercise["duration_min"]}, calories burned: {exercise["nf_calories"]}")
        add_exercise_row_to_sheet(exercise=exercise["name"], duration=exercise["duration_min"],
                                  calories=exercise["nf_calories"])


def add_exercise_row_to_sheet(exercise, duration, calories):
    global api_endpoint

    # authorization to access sheet
    headers = {
        "Authorization": f"Bearer {api_token}"
    }

    # save the current date and time of log entry
    date = datetime.now().date().strftime("%d/%m/%Y")
    time = datetime.now().time().strftime("%H:%M")

    # data to add to sheet row
    data = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise.title(),
            "duration": duration,
            "calories": calories
        }
    }

    # put the data in the sheet
    response = requests.post(
        url=api_endpoint,
        json=data,
        headers=headers
    )

    # check for success
    response.raise_for_status()
    print(response)