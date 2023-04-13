import i3ipc
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("--work")
args = parser.parse_args()

i3 = i3ipc.Connection()

if args.work == "regular":
    i3.command("exec firefox-developer-edition --new-tab https://www.youtube.com")
    time.sleep(1)
    
    i3.command("exec spotify")
    time.sleep(4)

    i3.command("exec discord")
    time.sleep(2)

    i3.command("exec telegram-desktop")


else:
    print("nope")