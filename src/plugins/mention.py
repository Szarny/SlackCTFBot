from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply


@respond_to("ctftime")
def mention_ctf_time(message):
    message.react("checkered_flag")
    message.reply("ctftime")


@respond_to("save")
def mention_help(message):
    message.react("pencil")
    message.reply("save")


@respond_to("ls")
def mention_ls(message):
    message.react("ok_hand")
    message.reply("ls")


@respond_to("help")
def mention_help(message):
    message.react("question")
    message.reply("help")