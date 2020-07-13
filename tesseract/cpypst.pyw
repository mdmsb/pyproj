import pyautogui
import pyperclip
import time
import tkinter as tk




def click_new():
    new_loc = None
    n = 0
    while new_loc == None:
        new_loc = pyautogui.locateOnScreen('new.png')
        time.sleep(0.4)
        n += 1
        if n == 20:
            sys.exit()
    loc = pyautogui.center(new_loc)
    print(loc)
    new_loc = pyautogui.locateOnScreen('new.png')
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
            sys.exit()
    loc = pyautogui.center(id_loc)
    print(loc)
    ##new_loc = pyautogui.locateOnScreen('new.png')
    x, y = loc
    pyautogui.click(x+30, y+8)







root = tk.Tk()
def paste_key(event):
    pyautogui.hotkey('win', '1')
    
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

B = tk.Button(root, text ="Paste", command = paste_key)
B.pack()
root.bind('p', paste_key)
root.bind('P', paste_key)
root.mainloop()
