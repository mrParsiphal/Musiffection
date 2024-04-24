def clear(text):
    return "\033[0m{}".format(text)


def fat(text):
    return "\033[1m{}\033[0m".format(text)


def fading(text):
    return "\033[2m{}\033[0m".format(text)


def italic(text):
    return "\033[3m{}\033[0m".format(text)


def underlined(text):
    return "\033[4m{}\033[0m".format(text)


def rarely_blink(text):
    return "\033[5m{}\033[0m".format(text)


def often_blink(text):
    return "\033[6m{}\033[0m".format(text)


def replacement(text):
    return "\033[7m{}\033[0m".format(text)


def black(text):
    return "\033[30m{}\033[0m".format(text)


def red(text):
    return "\033[31m{}\033[0m".format(text)


def green(text):
    return "\033[32m{}\033[0m".format(text)


def yellow(text):
    return "\033[33m{}\033[0m".format(text)


def blue(text):
    return "\033[34m{}\033[0m".format(text)


def violet(text):
    return "\033[35m{}\033[0m".format(text)


def turquoise(text):
    return "\033[36m{}\033[0m".format(text)


def white(text):
    return "\033[37m{}\033[0m".format(text)


def black_fon(text):
    return "\033[40m{}\033[0m".format(text)


def red_fon(text):
    return "\033[41m{}\033[0m".format(text)


def green_fon(text):
    return "\033[42m{}\033[0m".format(text)


def yellow_fon(text):
    return "\033[43m{}\033[0m".format(text)


def blue_fon(text):
    return "\033[44m{}\033[0m".format(text)


def violet_fon(text):
    return "\033[45m{}\033[0m".format(text)


def turquoise_fon(text):
    return "\033[46m{}\033[0m".format(text)


def white_fon(text):
    return "\033[47m{}\033[0m".format(text)
