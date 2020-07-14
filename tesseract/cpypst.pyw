import pyautogui
import pyperclip
import time
import tkinter as tk
import sys

from win32api import GetKeyState
from win32con import VK_CAPITAL, VK_NUMLOCK

if GetKeyState(VK_CAPITAL) == 1:
    pyautogui.press('capslock')
    print("Capslock turned off")
if GetKeyState(VK_NUMLOCK) == 1:
    pyautogui.press('numlock')
    print("Numlock turned off")



def click_new():
    new_loc = None
    n = 0
    while new_loc == None:
        new_loc = pyautogui.locateOnScreen('new.png')
        time.sleep(0.4)
        n += 1
        if n == 20:
            print("Exiting. . . Image not found")
            root.destroy()
            sys.exit()
    loc = pyautogui.center(new_loc)
    x, y = loc
    pyautogui.click(x+180, y+40)


def click_id():
    id_loc = None
    n = 0
    while id_loc == None:
        id_loc = pyautogui.locateOnScreen('id.png')
        time.sleep(0.4)
        n += 1
        if n == 20:
            print("Exiting. . . Image not found")
            root.destroy()
            sys.exit()
    loc = pyautogui.center(id_loc)
    x, y = loc
    pyautogui.click(x+30, y+8)




root = tk.Tk()
def paste_key():
    time.sleep(0.3)
    click_new()
    time.sleep(0.3)
    click_id()
    copied_text = pyperclip.paste()
    copied_text = copied_text.split("\t")
    ##print(copied_text[17],copied_text[18])
    m = copied_text[17]
    n = copied_text[18]
    copied_text[17] = n
    copied_text[18] = m
    ##print(copied_text[17],copied_text[18])
    print(copied_text)
    pyautogui.PAUSE = 0
    for ct in copied_text:
        pyautogui.write(ct)
        pyautogui.press(['tab'])


def p(event):
    time.sleep(0.5)
    pyautogui.hotkey('win', '1')
    time.sleep(0.1)
    paste_key()
    
    
def o(event):
    ##RUN SHORTCUT ON EXCEL
    time.sleep(0.5)
    pyautogui.hotkey('win', '2')
    time.sleep(0.1)
    pyautogui.press('down')
    time.sleep(0.1)

    pyautogui.hotkey('ctrl', 'shift', 'right')

    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)
    pyautogui.hotkey('win', '1')
    time.sleep(0.1)
    paste_key()



B1 = tk.Button(root, text ="P. Paste", command = p)
B1.pack()
B2 = tk.Button(root, text ="O. XL Copy + Paste", command = o)
B2.pack()
root.bind('p', p)
root.bind('P', p)
root.bind('o', o)
root.bind('O', o)
root.mainloop()
