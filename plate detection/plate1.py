import cv2
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd = "D:\\Program Files\\Tesseract-OCR\\tesseract"
cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
states = {"AN":"Andaman and Nicobar","AP":"Andhra Pradesh" ,"UP":"Uttar Pradesh","MP":"Madhya Pradesh","DL":"Delhi",
          "CH":"Chandigarh","HR":"Haryana","HP": "Himachal Pradesh","JK":"Jammu and Kashmir","MH":"Maharashtra",
          "MN":"Manipur","PN":"Punjab","WB":"West Bengal","RJ":"Rajasthan","CG":"Chattisgarh","TS":"Telangana",
          "DN":"Dadra and Nagar Haveli","PY":"Pondicherry","GJ":"Gujarat","AR":"Arunchal Pradesh","GA":"Goa",
          "KL":"Kerala","ML":"Meghalaya","LD":"Lakshadweep","NL":"Nagaland","OD":"Odisha",
          "SK":"Sikkim","TN":"Tamil Nadu","UK":"Uttarakhand","TR":"Tripura","MZ":"Mizoram","KA":"Karnatka","JH":"Jharkhand",
          "DD":"Daman and Diu","BR":"Bihar","AS":"Assam"}
def extract_num(img_name):
    global read
    img = cv2.imread(img_name)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    nplate = cascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in nplate:
        a,b = (int(0.02*img.shape[0])),int(0.025*img.shape[1])
        plate =img[y+a:y+h-a,x+b:x+w-b,:]
        kernel = np.ones((1,1),np.unit8)
        plate = cv2.dilate(plate,kernel,iterations=1)
        plate = cv2.erode(plate , kernel , iterations = 1)
        plate_gray = cv2.cvtColor(plate,cv2.COLOR_BGR2GRAY)
        (thresh,plate) = cv2.threshold(plate_gray,127,255,cv2.THRESH_BINARY)
        read = pytesseract.image_to_string(plate)
        print(read)
        read = ''.join(e for e in read if e.isalnum())
        stat = read[0:2]
        try:
            print("car belongs to",states[stat])
        except:
            print("State not recognised")
        print(read)
        cv2.rectangle(img,(x,y),(x+w,y+h),(51,51,255),2)
        cv2.rectangle(img, (x,y-40),(x+w,y),(51,51,255),-1)
        cv2.putText(img,read,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,)
        cv2.imshow('Plate',plate)
    cv2.imshow("result",img)
    cv2.imwrite('result.jpg',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

extract_num('D:/plate%20detection/1004194-bh-plate.webp')
