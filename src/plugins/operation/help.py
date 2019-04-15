def help_():
    return """:thinking_face: *How to use slack_ctf_bot* :thinking_face:

    usage: `@slack_ctf_bot <command> (<args>)`

    *Command*
    `ctftime <{web|static}>` : Show CTF events announced on CTFTime. :checkered_flag:
    `ls` : Show CTF events saved by members. :pencil:
    `save <title>|<date>` : Save CTF events. :pencil2:
    `rm <id>` : Remove CTF events from list that shown in `ls` command. :x:
    `help` : Show help message. :question:

    *Example*
    `save FooBarCTF|20190101-20191231`
    `rm abcde`
    
    *Note*
    Repository: https://github.com/Szarny/SlackCTFBot"""