"""
heli.py - Arian Mollik Wasi
MIT License

A simple script to print a helicopter animation to the terminal.
The heli_animation.txt file should be in the same folder as this file or else the code won't work

Usage
=====
To run normally use
    python heli.py
To specify a custom frame duration use
    python heli.py n
Where n is the duration such as 0.5:
    python heli.py 0.5
"""
import itertools
from os import name, system
from sys import argv
from time import sleep

# `cls` is a Windows command and `clear` is a Unix command to clear the terminal
CLEAR_COMMAND = "cls" if name == "nt" else "clear"
DELAY = float(argv[1]) if argv[1:] else 0.1


def clear():
    """Clear the terminal"""
    system(CLEAR_COMMAND)


with open("heli_animation.txt", encoding="utf-8") as f:
    # `itertools.cycle` creates a infinite iterable so the animation never stops
    # `i.strip("\n")` is there to remove trailing newlines
    # `filter(None, sequence)` removes all falsey elements such as empty strings
    # `f.read().split(...)` gets all the parts of the helicopter animation as a list
    helicopter_phases = itertools.cycle(
        [i.strip("\n") for i in filter(None, f.read().split("===================================="))]
    )

def print_heli():
    try:
        for heli_frame in helicopter_phases:
            print(heli_frame)
            # Since the value of the end parameter for `print()` is by default a newline
            # I can use a empty print without arguments to print only a newline
            print()
            # I add a `time.sleep` to delay the frames or else it will be too fast
            # I check if there is a custom delay passed and if not, it uses 0.1
            sleep(DELAY)
            # I clear the terminal after the run
            clear()
    except KeyboardInterrupt:
        print("Stopped!")

if __name__ == "__main__":
    print_heli()
    # One last clear just to be sure
    clear()
