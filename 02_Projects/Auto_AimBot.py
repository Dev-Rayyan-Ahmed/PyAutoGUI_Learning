import pyautogui as pyauto
import time
import win32api,win32con
import keyboard
import random

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


time.sleep(4)

# For Setup
# print(pyauto.position())
# ss = pyauto.screenshot(region=(352,198,1198,725))
# ss.save(r"C:\Coding (VScode)\Codes\.CodingTools\PyAutoGUI_Learning\02_Projects\game_board.png")

while keyboard.is_pressed('q') == False:

    pic = pyauto.screenshot(region=(352,198,1198,725))

    width, height = pic.size
    # Color: (255,87,34) RGB
    for x in range(0,width,5):
        for y in range(0,height,5):

            r,g,b = pic.getpixel((x,y))

            if r == 255 and g == 87 and b == 34:
                click(x+352,y+198)
                time.sleep(0.05)
                break


