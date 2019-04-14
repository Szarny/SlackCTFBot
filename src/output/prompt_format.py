from .pycolor import Pycolor

def prompt_format(color, mark, message):
    return "[" + color + mark + Pycolor.END + "]" + " " + message