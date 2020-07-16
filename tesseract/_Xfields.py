##import cv2 
##import pytesseract
##import image_process as ip
##import os
##import sys
import re





f = open("attachments/convtxt.txt","r")
txt = f.read()


def get_txt():
    txt_spl = txt.split("\n")
    list_data = []
    for ts in txt_spl:
        if ts[:4] == "9013":
            ts = ts.replace("\n"," ")
            list_data.append(ts)
    return list_data

list_data = get_txt()


parts = [[],[],[],[],[],[],[]]
for l in list_data:
    f = re.findall(r'^.*?[|].*?\d\d\d\d\d\d+[|]', l) ## MATCH ID , HOS NAME , HPN
    m = f[0]
    pipes = re.findall(r'[|]', m)
    if len(pipes) > 5:
        if m.find("N/A") > 0:
            m = m.split("N/A")[0]
            m = m + "N/A|"
##    print(m)
    parts[0].append(m)
    l = l.replace(m,"")
    
    f = re.findall(r'^.*?[|]\d\d\d[|]', l) ## MATCH ADDRESS, CITY, STATE, POSTAL, ZIP CODE, COUNTRY, LOC COUNTRY, LOC AREA CODE
    m = f[0]
##    print(m)
    parts[1].append(m)
    l = l.replace(m,"")

    f = re.findall(r'(^)(.*?)([|]\s*\D\s*[|])', l) ## MATCH  LOC FIPS, LOC MSA, LOC PMSA, LOC TZ, LOC DST
    m = f[0][0] + f[0][1] + f[0][2]
    parts[2].append(m)
##    print(m)
    l = l.replace(m,"")

    f = re.findall(r'(^)(.*?)([|])(.*?)([^|N/A][A-Za-z])', l) ## MATCH LOC LAT CENTROID, LOC LONG CENTROID, LOC LAT POLY, LOC LONG POLY
    m = f[0][1] + f[0][2] + f[0][3] + f[0][4]
    m = m.split("|")
    m.pop(-1)
    t = ""
    for n in m:
        t = t + n + "|"
##    print(t)
    parts[3].append(t)
    l = l.replace(t,"")

    f = re.findall(r'(^)(.*?)[(]', l) ## MATCH BIZ NAME , BIZ INFO
    m = f[0][1]
##    print(m)
    parts[4].append(m)
    l = l.replace(m,"")

    f = re.findall(r'[(]\d\d\d[)].*?[|]', l) ## MATCH BIZ PHONE, BIZ PHONE EXT, BIZ FAX, BIZ EMAIL
    if len(f) > 1:
        m = f[0] + "N/A|" + f[1] + "N/A|"
    else:
        m = f[0] + "N/A|N/A|N/A|"
##    print(m)
    parts[5].append(m)

    f = re.findall(r'[|][a-zA-Z][a-zA-Z].*?$', l) ## MATCH WEB URL, WEB META TITLE, WEB META DESC, WEB META KEY
    if len(f) == 0:
        f.append("|N/A|N/A|N/A|N/A|")
    f = f[0][1:]
##    print(f)
    parts[6].append(f)
    

##txt = ""
##for p in parts:
##    print(len(p))
##    for d in p:
##        txt = txt + d + "\n"
##f = open("attachments/fields.txt","w")
##f.write(txt)
##f.close()


data = [[],[],[],[],[],[],[],[],[],[],[]]

for p in parts[0]:
    p = p.replace("|"," ")
    p = p.split(" ")
    data[0].append(p[0])
    data[2].append(p[-2])
    m = ""
    for d in p[1:-2]:
        m = m + d + " "
    data[1].append(m[:-1])
    

for d in parts[1]:
    print(d)
    f = re.findall(r'[|]\D\D?\d?[|]', d)
##    d = d.split(f)
    print(f)
        
        




















##data = [[],[]]
##n = 0
##for l in list_data:
##    
##    
##    match = re.findall(r'(\n|^)([9013]\d+[|])', l)
##    data[0].append(match[0][1][:-1])
##
##    match = re.findall(r'(\n|^)([9013]\d+[|])(.*?)([|]\d)', l)
##    matched = match[0][2]
##    matched = matched.replace("|"," ")
##    matched = matched.replace(" N/A","")
##    list_data[n].replace()
##    n += 1
##    data[1].append(matched)
##
##    
##
##
##
##f = open("attachments/fields.txt","w")
##lst_d = ""
##i = 1
##for lst in data:
##    n = 0
##    lst_d = lst_d + "\nDATA#" + str(i) + "\n"
##    i += 1
##    for ls in lst:
##        if n < 3:
##            print(ls)
##            n += 1
##        lst_d = lst_d + ls + "\n"
##    
##f.write(lst_d)
##f.close()














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
    





































##def conv_txt(img):
##    print("Finding text from image")
##    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
##    custom_config = r'--oem 3 --psm 6'
##    txt = pytesseract.image_to_string(img, config=custom_config)
##    print("completed\n")
##    return txt
##
##
##
##def refine_img(image):
##    print("Refining Image")
##    gray = ip.get_grayscale(image)
##    thresh = ip.thresholding(gray)
##    print("Completed")
##    return thresh
##
##
##def convert(fl):
##    image = cv2.imread(fl)
##    img = refine_img(image)
##    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
##    txt = conv_txt(img)
##    return txt
##
##
##
##
##def clean_txt_regx(txt):
##    match = re.findall(r'\d+[.]*\s\d+', txt)
##    for m in match:
##        n = m.replace(" ","")
##        txt = txt.replace(m,n)
##    return txt
##
##def clean_txt(txt):
##    txt = txt.replace("”","")
##    txt = txt.replace("“","")
##    txt = txt.replace("’","")
##    txt = txt.replace('"',"")
##    txt = txt.replace("'","")
##    txt = txt.replace("\n","")
##    txt = txt.replace("¥","Y")
##    txt = txt.replace("€","E")
##    txt = txt.replace("US4","USA")
##    txt = txt.replace(",","|")
##    txt = txt.replace("| ","|")
##    txt = txt.replace(" |","|")
##    txt = txt.replace("||","|N/A|")
##    txt = txt.replace("||","|N/A|")
##    txt = txt.replace("9013","\n\n9013")
##    txt = clean_txt_regx(txt)
##    txt = clean_txt_regx(txt)
##    return txt
##
##
##
##
####def test_tess():
####    fl= "attachments/test.tif"
####    image = cv2.imread(fl)
####    img = refine_img(image)
####    imgsize = 1.5
####    print(imgsize)
####    img = cv2.resize(image, None, fx=imgsize, fy=imgsize, interpolation=cv2.INTER_CUBIC)
####
####    img = cv2.resize(img, None, fx=1, fy=2, interpolation=cv2.INTER_CUBIC)
####
####    cv2.imshow("resized dimension", img)
####    cv2.waitKey(0)
####    cv2.destroyAllWindows()
####
####    txt = conv_txt(img)
####    print(txt)
##
####test_tess()
##
##
##
##def list_files():
##    file = "attachments/"
##    files = os.listdir(file)
##
##    imgfile = []
##    for f in files:
##        if f[-3:] == "tif":
##            imgfile.append(f)
##            
##    print("\nFiles found = " + str(imgfile) + "\n")
##    match = re.findall(r'\d\d\d', str(imgfile))
##    match.sort()
##    
##    l = re.compile("\d\d\d").split(files[0])
##
##    myfiles = []
##    for m in match:
##        myfiles.append(str(file + l[0] + m + l[1]))
##    return myfiles
##
##
##def conv_dir_img():
##    print("Clearing 'convtxt.txt' file. . .")
##    f = open("convtxt.txt","w")
##    f.write("")
##    f.close()
##    print("Cleared")
##
##    files = list_files()
##    for f in files:
##        print(f)
##        txt = convert(f)
##        txt = clean_txt(txt)
##        f = open("convtxt.txt","a")
##        f.write(str(txt+"\n\n"))
##        f.close()
##            
####conv_dir_img()
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
