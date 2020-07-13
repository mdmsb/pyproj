import pyautogui
import pyperclip
import time

time.sleep(0.5)
pyautogui.hotkey('win', '1')
copied_text = pyperclip.paste()
copied_text = copied_text.split("\t")
##print(copied_text[17],copied_text[18])
m = copied_text[17]
n = copied_text[18]
copied_text[17] = n
copied_text[18] = m
##print(copied_text[17],copied_text[18])
print(copied_text)
time.sleep(0.5)
pyautogui.PAUSE = 0
for ct in copied_text:
    pyautogui.write(ct)
    pyautogui.press(['tab'])

