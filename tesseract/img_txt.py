import cv2 
import pytesseract
import image_process as ip
import os
import sys
import re




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
    txt = txt.replace("USA4","USA")
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
    print(match)
    l = re.compile("\d\d\d").split(imgfile[0])
    print(l)
    myfiles = []
    for m in match:
        myfiles.append(str(file + l[0] + m + l[1]))
    return myfiles


def conv_dir_img():
    print("Clearing 'convtxt.txt' file. . .")
    f = open("attachments/convtxt.txt","w")
    f.write("")
    f.close()
    print("Cleared")

    files = list_files()
    for f in files:
        print(f)
        txt = convert(f)
        txt = clean_txt(txt)
        f = open("attachments/convtxt.txt","a")
        f.write(str(txt+"\n\n"))
        f.close()
            
conv_dir_img()















