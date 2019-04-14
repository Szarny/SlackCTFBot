import pickle

def rm(rm_target_id):
    ctflist = []
    with open("db/ctfinfo.pickle", "rb") as f:
        ctflist = pickle.load(f)

    for idx, ctf in enumerate(ctflist):
        id_ = ctf["id_"]
        title = ctf["title"]
        date = ctf["date"]

        if id_ == rm_target_id:

            removed_ctflist = ctflist[:idx] + ctflist[idx+1:]
            with open("db/ctfinfo.pickle", "wb") as f:
                pickle.dump(removed_ctflist, f)

            return "*Delete*: `{id_}: {title} ({date})`".format(
                id_=id_,
                title=title,
                date=date
            )
    
    return "ID not found :cry:"