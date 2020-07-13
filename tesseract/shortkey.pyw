from pynput import keyboard
from tkinter import messagebox
import cpypst as cp

mylist = [keyboard.Key.alt_l, keyboard.KeyCode(char='s')]
current = []
def on_press(key):
    current.append(key)
    print(current, mylist)
    if mylist == current:
        print('match')
        cp.paste_key()
        
        

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        messagebox.showinfo("Shortkey", "Shortkey is stopped")
        return False
    else:
        current.remove(key)


# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

