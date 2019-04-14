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

    id_ = generate_id()

    ctflist.append({
        "id_": id_,
        "title": title,
        "date": date
    })

    with open("db/ctfinfo.pickle", "wb") as f:
        pickle.dump(ctflist, f)

    return "*Save* `{id_} {title} ({date})`".format(
        id_=id_,
        title=title,
        date=date
    )