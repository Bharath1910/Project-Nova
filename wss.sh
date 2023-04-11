#!/bin/bash

options="Option 1\nOption 2\nOption 3"
selected=$(echo -e "$options" | rofi -dmenu)

case $selected in
    "Option 1")
        # Replace this with the command you want to run for option 1
        ;;
    "Option 2")
        # Replace this with the command you want to run for option 2
        ;;
    "Option 3")
        # Replace this with the command you want to run for option 3
        ;;
esac