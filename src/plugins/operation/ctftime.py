import requests
from bs4 import BeautifulSoup


def ctftime(mode):
    if mode == "web":
        response = requests.get("https://ctftime.org/event/list/upcoming")
        soup = BeautifulSoup(response.text, "lxml")

    if mode == "static":
        with open("db/ctftime.html") as f:
            soup = BeautifulSoup(f.read(), "lxml")

    events = soup.findAll("tr").find_all("a")


    return events