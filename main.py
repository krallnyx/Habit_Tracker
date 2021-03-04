import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"


class HabitTracker:
    def __init__(self):
        user_params = {
            "token": "asdf54dsafg64sdf",
            "username": "krall",
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }
        response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
        print(response.text)


if __name__ == '__main__':
    habit_tracker = HabitTracker()
