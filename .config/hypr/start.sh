#!/usr/bin/env bash

# inityializing wallpaper daeom
swww init &
# setting wallpaper
swww img ~/.config/background

nm-applet --indicator &

# tyhe bar
waybar &

# notifications
dunst
