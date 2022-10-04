import pyautogui, sys
import time
import keyboard


a=input("start?")
if str(a) == ("yes"):
    while True:
        if keyboard.is_pressed("q"):
            while True:
                pyautogui.moveTo(970, 174, 2)
                pyautogui.moveTo(970, 700, 2)
