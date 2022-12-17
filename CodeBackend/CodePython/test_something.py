import face_recognition
import numpy as np

from dataset_procesing import load_dataset
dataset = load_dataset()
import os
dataset = load_dataset()
print(len(dataset['name']))
for i,value in enumerate(dataset['encoding']):
    results = face_recognition.compare_faces(dataset['encoding'], value, tolerance=0.45)
    confidents = face_recognition.face_distance(dataset['encoding'], value)
    # if true take name
    # list index true
    
    preson = [dataset['name'][index] for index, value in enumerate(results) if value == True]
    # print(preson)
    # print(confidents)
    print(len(preson))
    # print(confidents.mean())

    # break
    # if len(preson) > 5:
    #     path = 'dataset/' + preson[i] + '.npy'
    #     if os.path.exists(path): 
    #         os.remove(path)
    #         break
        


# list_preson = ['Go_Hye_Sun_0ID', 'Bao_Thanh_19', 'Sohee_(Wonder_Girl)_11', 'Vo_Huynh_Le_2', 'Canh_Diem__16', 'Bui_Thi_Hue_8', 'Ho_Kha_12', 'Duong_Duong_5', 'Nguyen_Thi_Thuy_Quanh_19', 'Gong_Seung_Yeon_17', 'Sooyoung_11', 'Eun_Hyuk_0ID', 'Himchan_(B', 'Vien_Lap_5', 'Van_Mai_Huong_11', 'Gong_Hyun_Joo_7', 'Dich_Duong_Thien_Ti_1', 'Changmin(TVXQ)_6', 'Son_Ye _Jin_7', 'Vu_Thanh_Thao_8', 'Chi_Pu_6', 'Hyuna(4Minute)_4', 'Nichkhun(2PM)_17', 'Chanyeol_EXO_6', 'Doan_Thi_Linh_Chi_9', 'Gayoon(4Minute)_4', 'Nhu_Quynh_1', 'HyunBin_0ID', 'Ngoc_Thao_17', 'So_Ji_Sub_18', 'Dang_Thuong_6', 'Ha_Canh_8', 'Han_Hyo_Joo_2', 'Hoa_Minzy_13']
