from nutritionix import NutritionixUser
from sheety import log_exercises

# create a user with default information
nutritionix_user = NutritionixUser()

# log an exercise in the Google workout sheet
log_exercises(nutritionix_user.get_nutritionix_response())