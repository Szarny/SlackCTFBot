from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

from .operation.save import save
from .operation.ls import ls
from .operation.rm import rm
from .operation.help import help_


@respond_to("ctftime")
def mention_ctf_time(message):
    message.react("checkered_flag")

    message.reply("ctftime")


@respond_to("save")
def mention_help(message):
    message.react("pencil2")

    title, date = message.body["text"].split()[1].split("|")
    result = save(title, date)
    message.reply(result)


@respond_to("rm")
def mention_help(message):
    message.react("x")

    rm_target_id = message.body["text"].split()[1]
    result = rm(rm_target_id)
    message.send(result)


@respond_to("ls")
def mention_ls(message):
    message.react("pencil")

    result = ls()
    message.send(result)


@respond_to("help")
def mention_help(message):
    message.react("question")

    result = help_()
    message.send(result)