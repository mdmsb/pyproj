import os

directory = "attachments/"
files = os.listdir(directory)

for f in files:
    if f[-3:] == "tif":
        if len(f) > 12:
            os.rename(str(directory+f),str(directory+f[-12:]))
            print(str(directory+f),str(directory+f[-12:]),"\n")
        else:
            print("file length is short\nMay be already renamed?", f, "\n")
print("completed")
