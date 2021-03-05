import requests
from datetime import datetime
USERNAME = "krall"
TOKEN = "asdf54dsafg64sdf"
GRAPH_NAME = "graph1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = F"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_CREATION_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_NAME}"



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
            "id": GRAPH_NAME,
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

        day = datetime.now().strftime("%Y%m%d")
        # alternatively if we want to populate for an past day :
        # day = datetime(year=2021, month=3, day=05).strftime("%Y%m%d")

        pixel_data = {
            "date": day,
            "quantity": "85",
        }
        # testing updating an existing pixel so adding one is commented
        # requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_data, headers=headers)

        update_endpoint = f"{PIXEL_CREATION_ENDPOINT}/{day}"

        new_pixel_data= {
            "quantity": "70"
        }
        # testing deleting an existing pixel so not updating anymore
        # requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)

        requests.delete(url=update_endpoint, headers=headers)


if __name__ == '__main__':
    habit_tracker = HabitTracker()
