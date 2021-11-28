"""
heli.py - Arian Mollik Wasi
MIT License

A simple script to print a helicopter animation to the terminal.
The heli_animation.txt file should be in the same folder as this file or else the code won't work
"""
import os
import itertools
import time


def clear():
    """Clear the terminal"""
    # `cls` is a Windows command and `clear` is a Unix command to clear the terminal
    os.system("cls" if os.name == "nt" else "clear")


with open("heli_animation.txt", encoding="utf-8") as f:
    # `itertools.cycle` creates a infinite iterable so the animation never stops
    # `i.strip("\n")` is there to remove trailing newlines
    # `filter(None, sequence)` removes all falsey elements such as empty strings
    # `f.read().split(...)` gets all the parts of the helicopter animation as a list
    helicopter_phases = itertools.cycle(
        [i.strip("\n") for i in filter(None, f.read().split("===================================="))]
    )

for heli_frame in helicopter_phases:
    print(heli_frame)
    # Since the value of the end parameter for `print()` is by default a newline
    # I can use a empty print without arguments to print only a newline
    print()
    # I add a `time.sleep` to delay the frames or else it will be too fast
    time.sleep(0.1)
    # I clear the terminal after the run
    clear()
# One last clear just to be sure
clear()
