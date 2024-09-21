import requests

# ----- https://opentdb.com/api.php?amount=10&type=boolean -----"
# From the API link we observe that there are some parameters after the ?
# This amount probably refers to the amount of questions in the quizz
# the other parameter is type = boolean, this is related to the questions we choose are
# True/False

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]
# print(question_data)

# Notas: The reason why we get 'AMC&#039;s is because html converts characters used in html
# programming language into entitys name and number, so it doesnt mess up with the code.