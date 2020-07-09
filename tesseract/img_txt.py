import cv2 
import pytesseract
import image_process as ip
import os
import sys




def conv_txt(img):
    print("Finding text from image")
    custom_config = r'--oem 3 --psm 6'
    txt = pytesseract.image_to_string(img, config=custom_config)
    print("completed")
    return txt



def refine_img(image):
    print("Refining Image")
    gray = ip.get_grayscale(image)
    thresh = ip.thresholding(gray)
    opening = ip.opening(gray)
    canny = ip.canny(gray)
    print("Completed")
    return thresh


def convert(fl):
    image = cv2.imread(fl)
    img = refine_img(image)
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    txt = conv_txt(img)
    return txt



def conv_dir_img():
    file = "/home/msb/Desktop/tesseract/attachments/"
    files = os.listdir(file)
    if (str(files).find('convtxt') > -1):
        print("converted text files will be overwritten, delete the files first. Exiting.")
        sys.exit()
    for f in files:
        if f[-3:] == "tif":
            fl = file + f
            print(fl)
            txt = convert(fl)
            f = open(str(fl[:-4] + "_convtxt.txt"), "w")
            f.write(txt)
            f.close
            
conv_dir_img()


















