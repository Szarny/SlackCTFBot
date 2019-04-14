from .pycolor import Pycolor
from .prompt_format import prompt_format


def info(message):
    print(prompt_format(Pycolor.GREEN, "*", message))


def ask(message):
    return input(prompt_format(Pycolor.GREEN, "?", message))


def add(message):
    print(prompt_format(Pycolor.BLUE, "+", message))


def warn(message):
    print(prompt_format(Pycolor.PURPLE, "-", message))


def error(message):
    print(prompt_format(Pycolor.RED, "!", message))
    print(prompt_format(Pycolor.RED, "!", "System terminated"))