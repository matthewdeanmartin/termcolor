import sys
from termcolor import colored, cprint
from termcolor.__main__ import demo


def test_exercise_code():
    text = colored("Hello, World!", "red", attrs=["reverse", "blink"])
    print(text)
    cprint("Hello, World!", "green", "on_red")

    def print_red_on_cyan(x):
        cprint(x, "red", "on_cyan")

    print_red_on_cyan("Hello, World!")
    print_red_on_cyan("Hello, Universe!")

    for i in range(10):
        cprint(i, "magenta", end=" ")

    cprint("Attention!", "red", attrs=["bold"], file=sys.stderr)


def test_examples():
    colored("Hello, World!", "red", "on_grey", ["bold", "blink"])
    colored("Hello, World!", "green")


def test_spurious_reset():
    hello = "Hello, World!"
    out = colored("Hello, World!")
    assert out == hello


def test_main():
    demo()
