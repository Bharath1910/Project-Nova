#!/bin/bash

options="Regular\nDevelopment\nOption 3"
selected=$(echo -e "$options" | rofi -dmenu)

case $selected in
    "Regular")
        python3 /home/bharath/Documents/Codes/projects/ProjectNova/wsExecute.py --work regular
        ;;
    "Development")
        python3 /home/bharath/Documents/Codes/projects/ProjectNova/wsExecute.py --work development
        ;;
    "Option 3")
        # Replace this with the command you want to run for option 3
        ;;
esac