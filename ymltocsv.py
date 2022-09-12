# 해당 프로그램은 rAthena 서버파일
# rAthena\db\re 폴더의 db 파일인 yml 파일에서
# ID, AegisNAme, Name 항목만 추출하여 CSV 파일로 만들어주는 프로그램임
#
# This program is extract ID, AegisName, Name from yml file 
# in rAthena\db\re folder, And make .CSV file
########################################################################
# Target yml file:
# item db : item_db, item_db_equip, item_db_etc, item_db_usable
# etc db : mob_db
#
# Output csv file form:
# ID, AegisName, Name
# 100, A, A, , ,
# 101, B, B, , ,
# ...


from tkinter import *
from tkinter import filedialog
from ymltocsv_func import yml_to_csv
import tkinter.messagebox as msgbox

root = Tk()
root.title("Database yml to csv") # 프로그램 제목타이틀
root.geometry("670x170+300+100") # 프로그램 해상도
root.resizable(False, False) # 프로그램 크리 변경 불가

# dir path 함수 정의
def dir_path():
    folder_dir = filedialog.askdirectory()
    if folder_dir == '': #사용자가 취소를 누를 때
        return
    #prunt(folder_selected)
    RE_dir_path.delete(0, END)
    RE_dir_path.insert(0, folder_dir)

try:
    # 타이틀, 제작자, 블로그, 입력설명
    titlename = Label(root, text="rAhtena database - yml to csv (ID, AegisName, Name)", font="arial 16 bold") #제목
    titlename.place(x=73, y=15)
    makers = Label(root, text="제작자 : SerG") #제작자
    makers.place(x=580, y=120)
    blogs = Label(root, text="https://blog.naver.com/hihihi0102") #블로그주소
    blogs.place(x=467, y=140)
    dir_path_desc = Label(root, text="rAthena\\db\\re 폴더 경로 입력") #입력창설명
    dir_path_desc.place(x=14, y=60)

    # RE 폴더 경로
    RE_dir_path = Entry(root, width=80)
    RE_dir_path.place(x=15, y=84)

    # 찾기 버튼
    btn1_dirpath = Button(root, width=8, text="찾기", relief="raised", command=dir_path)
    btn1_dirpath.place(x=590, y=80)

    # 시작버튼
    btn2_start = Button(root, padx=10, pady=1, text="yml to csv", font="arial 10", command=lambda:yml_to_csv(RE_dir_path.get() + "\\"))
    btn2_start.place(x=310, y=120)
except Exception as err: #예외처리
    msgbox.showerror("에러", err)

root.mainloop()
