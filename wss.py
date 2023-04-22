#!/home/bharath/.pyenv/versions/projectNova/bin/python

from pydymenu import rofi
import os

basePath = "/home/bharath/Documents/Codes/projects/ProjectNova"
workspaces = ["development", "regular"]
selectedWorkspace = rofi(workspaces, prompt="Select workspace")


if selectedWorkspace[0] == "regular":
    os.system(f"python3 {basePath}/wsExecute.py --work regular")

elif selectedWorkspace[0] == "development":
    os.system(f"python3 {basePath}wsExecute.py --work development")
