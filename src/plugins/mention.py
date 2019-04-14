from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

from .operation.save import save
from .operation.ls import ls


@respond_to("ctftime")
def mention_ctf_time(message):
    message.react("checkered_flag")
    message.reply("ctftime")


@respond_to("save")
def mention_help(message):
    message.react("pencil")

    title, date = message.body["text"].split()[1].split("|")
    save(title=title, date=date)

    message.reply("save")


@respond_to("rm")
def mention_help(message):
    message.react("x")
    message.reply("rm")


@respond_to("ls")
def mention_ls(message):
    message.react("ok_hand")

    message.send("--- CTF List ---")
    message.send(ls())


@respond_to("help")
def mention_help(message):
    message.react("question")
    message.reply("help")