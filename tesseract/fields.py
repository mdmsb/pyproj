import cv2 
import pytesseract
import image_process as ip
import os
import sys
import re





f = open("convtxt.txt","r")
txt = f.read()


def get_txt():
    txt_spl = txt.split("\n")
    list_data = []
    for ts in txt_spl:
        if ts[:4] == "9013":
            list_data.append(ts)
    return list_data

list_data = get_txt()

for l in list_data:
    l = l.replace("\n"," ")
    f = re.findall(r'([|])', l)
    print(len(f))
















##f = open("convtxt.txt","r")
##txt = f.read()
##
##
##def get_txt():
##    txt_spl = txt.split("\n")
##    list_data = []
##    for ts in txt_spl:
##        if ts[:4] == "9013":
##            list_data.append(ts)
##    return list_data
##    
##
##
##
##list_data = get_txt()
##i = 0
##for l in list_data:
##    f = re.findall(r'(^\d+[|])(.*?)([|]\d)', l)
##    m = f[0][1] + f[0][2][:-2]
##    n = m
##    if m.find("|N/A") > 0:
##        m = m.split("|N/A")
##        m = m[0]
##        n = n[:-4]
##    if len(re.findall(r'\d\d\d\d\d\d\d\d*', m)) > 0:
##        m = m[:m.rfind(" ")] + "|" + m[m.rfind(" ")+1:]
##    else:
##        m = m.replace("|",",")
##
##    l = l.replace(n,m)
##    l = l.replace("\n"," ")
##    list_data[i] = l
##    i += 1
##
##for l in list_data:
##    l = l.split("|")
##    print(l[3])
##





##match = re.findall(r'(\n|^)([9013]\d+[|])(.*?)(\D[|]\d)', txt)
##
##for m in match:
##    m = m[2] + m[3][:-2]
##    na_val = m.find("|N/A")
##    if na_val > 0:
##        biz_name = m[:-4].replace("|",",")
##    else:
##        biz_name = m.replace("|",",")
##    print(biz_name)
##    txt = txt.replace(m,biz_name)





##for l in list_data:
##    print(l[2])
    





































def conv_txt(img):
    print("Finding text from image")
    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
    custom_config = r'--oem 3 --psm 6'
    txt = pytesseract.image_to_string(img, config=custom_config)
    print("completed\n")
    return txt



def refine_img(image):
    print("Refining Image")
    gray = ip.get_grayscale(image)
    thresh = ip.thresholding(gray)
    print("Completed")
    return thresh


def convert(fl):
    image = cv2.imread(fl)
    img = refine_img(image)
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    txt = conv_txt(img)
    return txt




def clean_txt_regx(txt):
    match = re.findall(r'\d+[.]*\s\d+', txt)
    for m in match:
        n = m.replace(" ","")
        txt = txt.replace(m,n)
    return txt

def clean_txt(txt):
    txt = txt.replace("”","")
    txt = txt.replace("“","")
    txt = txt.replace("’","")
    txt = txt.replace('"',"")
    txt = txt.replace("'","")
    txt = txt.replace("\n","")
    txt = txt.replace("¥","Y")
    txt = txt.replace("€","E")
    txt = txt.replace("US4","USA")
    txt = txt.replace(",","|")
    txt = txt.replace("| ","|")
    txt = txt.replace(" |","|")
    txt = txt.replace("||","|N/A|")
    txt = txt.replace("||","|N/A|")
    txt = txt.replace("9013","\n\n9013")
    txt = clean_txt_regx(txt)
    txt = clean_txt_regx(txt)
    return txt




##def test_tess():
##    fl= "attachments/test.tif"
##    image = cv2.imread(fl)
##    img = refine_img(image)
##    imgsize = 1.5
##    print(imgsize)
##    img = cv2.resize(image, None, fx=imgsize, fy=imgsize, interpolation=cv2.INTER_CUBIC)
##
##    img = cv2.resize(img, None, fx=1, fy=2, interpolation=cv2.INTER_CUBIC)
##
##    cv2.imshow("resized dimension", img)
##    cv2.waitKey(0)
##    cv2.destroyAllWindows()
##
##    txt = conv_txt(img)
##    print(txt)

##test_tess()



def list_files():
    file = "attachments/"
    files = os.listdir(file)

    imgfile = []
    for f in files:
        if f[-3:] == "tif":
            imgfile.append(f)
            
    print("\nFiles found = " + str(imgfile) + "\n")
    match = re.findall(r'\d\d\d', str(imgfile))
    match.sort()
    
    l = re.compile("\d\d\d").split(files[0])

    myfiles = []
    for m in match:
        myfiles.append(str(file + l[0] + m + l[1]))
    return myfiles


def conv_dir_img():
    print("Clearing 'convtxt.txt' file. . .")
    f = open("convtxt.txt","w")
    f.write("")
    f.close()
    print("Cleared")

    files = list_files()
    for f in files:
        print(f)
        txt = convert(f)
        txt = clean_txt(txt)
        f = open("convtxt.txt","a")
        f.write(str(txt+"\n\n"))
        f.close()
            
##conv_dir_img()















