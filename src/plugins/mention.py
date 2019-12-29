from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

from plugins.operation import ctftime, help

@respond_to("ctftime")
def mention_ctf_time(message):
    message.react("checkered_flag")

    ctfs = ctftime.get_ctfs()
    message.send(ctfs)


@respond_to("help")
def mention_help(message):
    message.react("question")

    result = help.help_()
    message.send(result)