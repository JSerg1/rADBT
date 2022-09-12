import tkinter.messagebox as msgbox
import os
import csv

def insert_korean(txt_path, csv_path):
    print(txt_path) # ko 아이템 db 경로 확인
    print(csv_path) # 추출 csv db 경로 확인
    dir = os.path.dirname(csv_path) 
    filename1 = os.path.basename(csv_path)
    ko_csv = open(txt_path, 'r', newline='', encoding="cp949") # ko 아이템 db 파일 열기
    eg_csv = open(csv_path, 'r', newline='', encoding="cp949") # 추출 csv db 열기
    new_csv = open(dir + '\\merged_' + filename1, 'w') # 저장할 csv 파일 이름 및 경로 설정(같은폴더 강제, 앞에  merged_ 붙음)
    ko_csv_read = list(csv.reader(ko_csv))
    en_csv_read = list(csv.reader(eg_csv))
    
    for i in en_csv_read:
        temp_val1 = i
        id1 = temp_val1[0]
        en_aegis_name = temp_val1[1]
        en_item_name = temp_val1[2]
        save_ko_aegis_name = temp_val1[3] # save_ko_aegis_name, save_ko_item_name 은 기본적으로 추출한 csv 파일의 trans 열이므로, 디폴트는 null 값임
        save_ko_item_name = temp_val1[4]
        for j in ko_csv_read:
            temp_var2 = j
            id2 = temp_var2[0]
            ko_aegis_name = temp_var2[1]
            ko_item_name = temp_var2[2]
            if id1 == id2: # id1 과 id2의 확인작업을 거친 후, id 넘버가 일치하는 항목만 save_ko_aegis_name, save_ko_item_name 항목에 한글 db 명을 넣음.
                save_ko_aegis_name = ko_aegis_name
                save_ko_item_name = ko_item_name
        new_csv.write(str(id1) + ',' + str(en_aegis_name) + ',' + str(en_item_name) + ',' + str(save_ko_aegis_name) + ',' + str(save_ko_item_name) + '\n')
    
    ko_csv.close()
    eg_csv.close()
    new_csv.close()
    
    msgbox.showinfo("Complite", "한글 파일과 합치는 작업이 완료되었습니다.")

# This code used only test
# test_val1 = 'C:/Users/Lee/Desktop/PythonWorkspace/rADBTP/korean_insert/ko_item_db.csv'
# test_val2 = 'C:/Users/Lee/Desktop/PythonWorkspace/rADBTP/korean_insert/item_db_equip.csv'
# insert_korean(test_val1, test_val2)