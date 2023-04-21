#!/home/bharath/.pyenv/versions/projectNova/bin/python

from pydymenu import rofi
import os

workspaces = ["development", "regular"]
selectedWorkspace = rofi(workspaces, prompt="Select workspace")


if selectedWorkspace[0] == "regular":
    os.system("python3 /home/bharath/Documents/Codes/projects/ProjectNova/wsExecute.py --work regular")

elif selectedWorkspace[0] == "development":
    os.system("python3 /home/bharath/Documents/Codes/projects/ProjectNova/wsExecute.py --work development")
