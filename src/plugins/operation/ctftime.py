import requests
from bs4 import BeautifulSoup


def get_ctfs():
    response = requests.get("https://ctftime.org/event/list/upcoming",
                             headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"})

    soup = BeautifulSoup(response.text, "html.parser")
    events = soup.findAll("tr")[1:]

    result = []
    for event in events:
        result.append((event.find("a").text, event.find_all("td")[1].text))

    ctfs = "\n".join(["- *{}* ({})".format(r[0], r[1]) for r in result])
    return ctfs