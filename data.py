import requests

API_URL = "https://opentdb.com/api.php?amount=10"

def get_questions():
    response = requests.get(API_URL)
    data = response.json()
    question_data = data['results']
    return question_data
