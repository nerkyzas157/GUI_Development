import requests  # type: ignore

parameters = {
    "amount": 10,
    "type": "boolean",
    # "category": 18 -> CS realted questions
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
