from slackbot.bot import Bot as SlackBot

from output import output


def main():
    slackbot = SlackBot()
    slackbot.run()


if __name__ == "__main__":
    output.info("Slack Bot is activated.")
    main()