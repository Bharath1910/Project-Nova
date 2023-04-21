#!/home/bharath/.pyenv/versions/projectNova/bin/python

import i3ipc
import argparse
import time
import os

parser = argparse.ArgumentParser()
parser.add_argument("--work")
args = parser.parse_args()

i3 = i3ipc.Connection()

def openApps(payload):
    for app, delay in payload:
        i3.command(app)
        time.sleep(delay)

if args.work == "regular":
    openApps([
        ["exec firefox-developer-edition --new-tab https://www.youtube.com", 5],
        ["exec spotify", 4],
        ["exec discord", 2],
        ["exec telegram-desktop", 0]
    ])

if args.work == "development":
    os.system("/home/bharath/Documents/Codes/projects/ProjectNova/handleProject.py")
    openApps([
        ["exec spotify", 0],
        ["exec alacritty", 0]
    ])

else:
    print("nope")