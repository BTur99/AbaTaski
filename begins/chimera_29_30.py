from sys import exit
from math import pi
from time import sleep


downloading = ["—", "/", "|", "\\"]
pi = round(pi, 2)


def from_grad_to_rad(grad):
    if grad < 0 or grad > 360:
        exit(1)

    return f"grad = {grad} --> rad = {grad * (pi / 180)}"


def from_rad_to_grad(rad):
    if rad < 0 or rad > (2 * pi):
        exit(1)

    return f"rad = {rad} --> grad = {rad * (180 / pi)}"


def endless_downloading_process():
    i = 0
    while i <= 3:
        print(f"\rПрогружаем... {downloading[i]}", end="")
        i += 1
        if i == 4:
            i = 0
        sleep(0.2)


print(endless_downloading_process())