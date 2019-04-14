import pickle
import hashlib
from datetime import datetime


def generate_id():
    now = datetime.today().strftime('%Y%m%d%H%M%S')

    return hashlib.sha256(now.encode()).hexdigest()[:5]


def save(title, date):
    ctflist = []

    with open("db/ctfinfo.pickle", "rb") as f:
        ctflist = pickle.load(f)

    ctflist.append({
        "id_": generate_id(),
        "title": title,
        "date": date
    })

    with open("db/ctfinfo.pickle", "wb") as f:
        pickle.dump(ctflist, f)