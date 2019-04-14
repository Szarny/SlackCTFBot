import pickle

def ls():
    ctflist = []
    with open("db/ctfinfo.pickle", "rb") as f:
        ctflist = pickle.load(f)

    reply_message = ":checkered_flag: *CTF List* :checkered_flag:\n"
    message_tmpl = "- {id_}: {title} ({date})\n"
    for ctf in ctflist:
        reply_message += message_tmpl.format(
            id_=ctf["id_"],
            title=ctf["title"],
            date=ctf["date"]
        )

    return reply_message