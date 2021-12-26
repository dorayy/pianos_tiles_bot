#website url :
#https://h5.4j.com/games/Piano-Tiles-2-Online/index.html?pubid=yiv&v=1546731466

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

print("Running the script")

#Click function in order to apply left click mouse touch on the position called
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
#Press q touch to leave
while keyboard.is_pressed('q') == False:
    #tiles col 1 position
    if pyautogui.pixel(850, 550)[0] == 0:
        click(850, 550)
    #tiles col 2 position
    if pyautogui.pixel(727, 550)[0] == 0:
        click(727, 550)
    #tiles col 3 position
    if pyautogui.pixel(595, 550)[0] == 0:
        click(595, 550)
    #tiles col 4 position
    if pyautogui.pixel(450, 550)[0] == 0:
        click(450, 550)
