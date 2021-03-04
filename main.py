import requests

USERNAME = "krall"
TOKEN = "asdf54dsafg64sdf"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = F"{PIXELA_ENDPOINT}/{USERNAME}/graphs"


class HabitTracker:
    def __init__(self):
        user_params = {
            "token": TOKEN,
            "username": USERNAME,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }
        # user creation not required anymore as already sent and now only returning a "user already exists"
        # requests.post(url=PIXELA_ENDPOINT, json=user_params)

        graph_config = {
            "id": "graph1",
            "name": "Cycling Graph",
            "unit": "Km",
            "type": "float",
            "color": "ajisai"
        }
        headers = {
            "X-USER-TOKEN": TOKEN
        }

        # Graph already created and visible at https://pixe.la/v1/users/krall/graphs/graph1.html
        # requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)


if __name__ == '__main__':
    habit_tracker = HabitTracker()
