"""ANSI Color formatting for output in terminal."""

from __future__ import print_function

import os

__ALL__ = ["colored", "cprint"]

# See package/pyproject.toml for version number

ATTRIBUTES = dict(
    list(
        zip(
            ["bold", "dark", "", "underline", "blink", "", "reverse", "concealed"],
            list(range(1, 9)),
        )
    )
)
del ATTRIBUTES[""]

HIGHLIGHTS = dict(
    list(
        zip(
            [
                "on_grey",
                "on_red",
                "on_green",
                "on_yellow",
                "on_blue",
                "on_magenta",
                "on_cyan",
                "on_white",
            ],
            list(range(40, 48)),
        )
    )
)

COLORS = dict(
    list(
        zip(
            [
                "grey",
                "red",
                "green",
                "yellow",
                "blue",
                "magenta",
                "cyan",
                "white",
            ],
            list(range(30, 38)),
        )
    )
)

RESET = "\033[0m"


def colored(text, color=None, on_color=None, attrs=None):
    """Colorize text.

    Available text colors:
        red, green, yellow, blue, magenta, cyan, white.

    Available text highlights:
        on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white.

    Available attributes:
        bold, dark, underline, blink, reverse, concealed.

    Example:
    >>> colored('Hello, World!', 'red', 'on_grey', ['bold', 'blink'])
    '\\x1b[5m\\x1b[1m\\x1b[40m\\x1b[31mHello, World!\\x1b[0m'

    >>> colored('Hello, World!', 'green')
    '\\x1b[32mHello, World!\\x1b[0m'
    """
    if os.getenv("ANSI_COLORS_DISABLED") is None:
        fmt_str = "\033[%dm%s"
        if color is not None:
            text = fmt_str % (COLORS[color], text)

        if on_color is not None:
            text = fmt_str % (HIGHLIGHTS[on_color], text)

        if attrs is not None:
            for attr in attrs:
                text = fmt_str % (ATTRIBUTES[attr], text)

        text += RESET
    return text


def cprint(text, color=None, on_color=None, attrs=None, **kwargs):
    """Print colorize text.

    It accepts arguments of print function.
    """

    print((colored(text, color, on_color, attrs)), **kwargs)
