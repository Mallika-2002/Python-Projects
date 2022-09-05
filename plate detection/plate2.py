import pytesseract
import matplotlib.pyplot as plt
import cv2
import glob
import os
file_path = os.getcwd() +"/download.jpg"
np_list =[]
predicted_np =[]
for file in glob.glob(file_path,recursive=True):
    np_file = file_path.split('/')[-1]
    number_plate =os.path.splitext(np_file)
    np_list.append(number_plate)
    np_img = cv2.imread(file_path)
    predicted_res = pytesseract.image_to_string(np_img,lang="eng",config='--oem   3   --psm   6   -c tessedit_char_whitelist=ABCDEFGHIJKLMOPQRSTUVWXYZ0123456789')
    filter_predicted_res = "".join(predicted_res.split()).replace(":","").replace("-","")
    predicted_np.append(filter_predicted_res)
print("original nuber plate","\t","predicted number plate","\t","accuracy")
print("-------------------","\t","--------------------","\t","----------")
def estimate_predicated_accuracy(ori_list,pre_list):
    for ori_plate,pre_plate in zip(ori_list,pre_list):
        acc="0%"
        number_matches = 0
        if ori_plate ==pre_plate:
            acc="100%"
        else:
            if len(ori_plate)==len(pre_plate):
                for o,p in zip(ori_plate,pre_plate):
                    if o==p:
                        number_matches+=1
                acc=str(round((number_matches/len(ori_plate)),2)*100)
                acc+="%"
            print(ori_plate,"\t",pre_plate,"\t",acc)
estimate_predicated_accuracy(np_list,predicted_np)
