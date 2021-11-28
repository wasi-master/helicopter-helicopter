import os
import itertools
import time


def clear():
    # `cls` is a Windows command and `clear` is a Unix command
    os.system("cls" if os.name == "nt" else "clear")


with open("heli_animation.txt", encoding="utf-8") as f:
    helicopter_phases = itertools.cycle(list(filter(None, f.read().split("===================================="))))

i = 0
while True:
    print(i)
    print(next(helicopter_phases))
    time.sleep(0.25)
    clear()
    i += 1
