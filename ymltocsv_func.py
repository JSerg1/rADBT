import tkinter.messagebox as msgbox
import os.path as os
import yaml

def yml_to_csv(dir):
    # 폴더 내 파일 체크 변수
    equip_check = os.isfile(dir + 'item_db_equip.yml')
    etc_check = os.isfile(dir + 'item_db_etc.yml')
    item_check = os.isfile(dir + 'item_db.yml')
    usabe_check = os.isfile(dir + 'item_db_usable.yml')
    mob_check = os.isfile(dir + 'mob_db.yml')
    
    comp_val = 0

    # item_db_equip.yml 파일 존재 체크 및 csv 변환
    if equip_check:
        print("item_db_equip 파일 존재 확인")
        with open(dir + 'item_db_equip.yml') as equipy:
            equip_val = yaml.load(equipy, Loader=yaml.FullLoader)
            equip_body = list(equip_val['Body'])
            equip_body_lenth = len(equip_body)
            
            equip_csv = open(dir + 'item_db_equip.csv', "w", encoding="UTF-8")
            equip_csv.write('ID' + ',' + 'AeigsName' + ',' + 'Name' + ',' + 'Trans_AeigsName' + ',' + 'Trans_Name' + '\n')
            
            for i in range(equip_body_lenth):
                equip_Keys = equip_body[i]
                equip_id_val = equip_Keys['Id']
                equip_Aegis_val = equip_Keys['AegisName']
                equip_Name_val = equip_Keys['Name']
                equip_csv.write(str(equip_id_val) + ',' + str(equip_Aegis_val) + ',' + str(equip_Name_val) + '\n')
            
            equip_csv.close()
            comp_val += 1
    else:
        print("item_db_equip 파일 없음")

    # item_db_etc.yml 파일 존재 체크 및 csv 변환
    if etc_check:
        print("item_db_etc 파일 존재 확인")
        with open(dir + 'item_db_etc.yml') as etcy:
            etc_val = yaml.load(etcy, Loader=yaml.FullLoader)
            etc_body = list(etc_val['Body'])
            etc_body_lenth = len(etc_body)
            
            etc_csv = open(dir + 'item_db_etc.csv', "w", encoding="UTF-8")
            etc_csv.write('ID' + ',' + 'AeigsName' + ',' + 'Name' + ',' + 'Trans_AeigsName' + ',' + 'Trans_Name' + '\n')
            
            for i in range(etc_body_lenth):
                etc_Keys = etc_body[i]
                etc_id_val = etc_Keys['Id']
                etc_Aegis_val = etc_Keys['AegisName']
                etc_Name_val = etc_Keys['Name']
                etc_csv.write(str(etc_id_val) + ',' + str(etc_Aegis_val) + ',' + str(etc_Name_val) + '\n')
            
            etc_csv.close()
            comp_val += 1
    else:
        print("item_db_etc 파일 없음")

    # item_db.yml 파일 존재 체크 및 csv 변환
    if item_check:
        print("item_db 파일 존재 확인")
        with open(dir + 'item_db.yml') as db:
            db_val = yaml.load(db, Loader=yaml.FullLoader)
            if 'Body' in db_val:
                db_body = list(db_val['Body'])
                db_body_lenth = len(db_body)
            
                db_csv = open(dir + 'item_db.csv', "w", encoding="UTF-8")
                db_csv.write('ID' + ',' + 'AeigsName' + ',' + 'Name' + ',' + 'Trans_AeigsName' + ',' + 'Trans_Name' + '\n')
            
                for i in range(db_body_lenth):
                    db_Keys = etc_body[i]
                    db_id_val = db_Keys['Id']
                    db_Aegis_val = db_Keys['AegisName']
                    db_Name_val = db_Keys['Name']
                    db_csv.write(str(db_id_val) + ',' + str(db_Aegis_val) + ',' + str(db_Name_val) + '\n')
            
                db_csv.close()
                comp_val += 1
            else:
                print("item_db는 있으나, Body 해쉬 없음")
    else:
        print("item_db 파일 없음")
    
    # item_db_usable.yml 파일 존재 체크 및 csv 변환
    if usabe_check:
        print("item_db_usable 파일 존재 확인")
        with open(dir + 'item_db_usable.yml') as usable:
            usable_val = yaml.load(usable, Loader=yaml.FullLoader)
            usable_body = list(usable_val['Body'])
            usable_body_lenth = len(usable_body)
            
            usable_csv = open(dir + 'item_db_usable.csv', "w")
            usable_csv.write('ID' + ',' + 'AeigsName' + ',' + 'Name' + ',' + 'Trans_AeigsName' + ',' + 'Trans_Name' + '\n')
            
            for i in range(usable_body_lenth):
                usable_Keys = usable_body[i]
                usable_id_val = usable_Keys['Id']
                usable_Aegis_val = usable_Keys['AegisName']
                usable_Name_val = usable_Keys['Name']
                usable_csv.write(str(usable_id_val) + ',' + str(usable_Aegis_val) + ',' + str(usable_Name_val) + '\n')
            
            usable_csv.close()
            comp_val += 1
    else:
        print("item_db_usable 파일 없음")

    # mob_db.yml 파일 존재 체크 및 csv 변환
    if mob_check:
        print("mob_db 파일 존재 확인")
        with open(dir + 'mob_db.yml') as mob:
            mob_val = yaml.load(mob, Loader=yaml.FullLoader)
            mob_body = list(mob_val['Body'])
            mob_body_lenth = len(mob_body)
            
            mob_csv = open(dir + 'mob_db.csv', "w", encoding="UTF-8")
            mob_csv.write('ID' + ',' + 'AeigsName' + ',' + 'Name' + ',' + 'Trans_AeigsName' + ',' + 'Trans_Name' + '\n')
            
            for i in range(mob_body_lenth):
                mob_Keys = mob_body[i]
                mob_id_val = mob_Keys['Id']
                mob_Aegis_val = mob_Keys['AegisName']
                mob_Name_val = mob_Keys['Name']
                mob_csv.write(str(mob_id_val) + ',' + str(mob_Aegis_val) + ',' + str(mob_Name_val) + '\n')
            
            mob_csv.close()
            comp_val += 1
    else:
        print("mob_db 파일 없음")


    msgbox.showinfo("Complite", str(comp_val) + "개의 yml 파일이 CSV 파일로 변환이 완료되었습니다.")
