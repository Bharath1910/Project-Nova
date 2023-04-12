#!/bin/bash

options="Option 1\nOption 2\nOption 3"
selected=$(echo -e "$options" | rofi -dmenu)

case $selected in
    "Regular")
        python3 /home/bharath/Documents/Codes/projects/ProjectNova/wsExecute.py --work regular
        ;;
    "Option 2")
        # Replace this with the command you want to run for option 2
        ;;
    "Option 3")
        # Replace this with the command you want to run for option 3
        ;;
esac