import tkinter.messagebox as msgbox
import os
import csv

def insert_korean(txt_path, csv_path):
    print(txt_path)
    print(csv_path)
    dir = os.path.dirname(csv_path)
    filename1 = os.path.basename(csv_path)
    ko_csv = open(txt_path, 'r', newline='', encoding="cp949")
    eg_csv = open(csv_path, 'r', newline='', encoding="cp949")
    new_csv = open(dir + '\\merged_' + filename1, 'w')
    new_csv.write('ID' + ',' + 'AeigsName' + ',' + 'Name' + ',' + 'Trans_AeigsName' + ',' + 'Trans_Name' + '\n')
    ko_csv_read = csv.reader(ko_csv)
    en_csv_read = list(csv.reader(eg_csv))
    
    for i in ko_csv_read:
        ko_val = i
        id1 = ko_val[0]
        aegis_name1 = ko_val[1]
        item_name1 = ko_val[2]
        for j in en_csv_read:
            eg_val = j
            id2 = eg_val[0]
            aegis_name2 = eg_val[1]
            item_name2 = eg_val[2]
            if id1 == id2:
                new_csv.write(str(id1) + ',' + str(aegis_name1) + ',' + str(item_name1) + ',' + str(aegis_name2) + ',' + str(item_name2) + '\n')
                
    msgbox.showinfo("Complite", "한글 파일과 합치는 작업이 완료되었습니다.")

# This code used only test
# test_val1 = 'C:/Users/Lee/Desktop/PythonWorkspace/rADBTP/korean_insert/ko_item_db_test1_kr.csv'
# test_val2 = 'C:/Users/Lee/Desktop/PythonWorkspace/rADBTP/korean_insert/ko_item_db_test2_eg.csv'
# insert_korean(test_val1, test_val2)