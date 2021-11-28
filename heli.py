import os
import itertools
import time


def clear():
    # `cls` is a Windows command and `clear` is a Unix command
    os.system("cls" if os.name == "nt" else "clear")


with open("heli_animation.txt", encoding="utf-8") as f:
    helicopter_phases = itertools.cycle(
        [i.strip("\n") for i in filter(None, f.read().split("===================================="))]
    )


while True:
    print(next(helicopter_phases))
    print()
    time.sleep(0.1)
    clear()
