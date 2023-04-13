import i3ipc
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("--work")
args = parser.parse_args()

i3 = i3ipc.Connection()

def execute(payload):
    for app, delay in payload:
        i3.command(app)
        time.sleep(delay)

if args.work == "regular":
    execute([
        ["exec firefox-developer-edition --new-tab https://www.youtube.com", 5],
        ["exec spotify", 4],
        ["exec discord", 2],
        ["exec telegram-desktop", 0]
    ])

    # i3.command("exec firefox-developer-edition --new-tab https://www.youtube.com")
    # time.sleep(2)
    
    # i3.command("exec spotify")
    # time.sleep(4)

    # i3.command("exec discord")
    # time.sleep(2)

    # i3.command("exec telegram-desktop")

else:
    print("nope")