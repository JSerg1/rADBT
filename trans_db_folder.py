# 3번 프로그램
# db 폴더내 yml 파일을
# input 해주는 csv 파일의 한글 aegisname, 한글 itemname 항목으로
# 바꿔주는 프로그램
#
# 사용 가능한 Input file (able to use only csv)
# Item 부분 (4개)
#  - Item_db , Item_db_etc , Item_db_usable , Item_db
# Monster 부분 (1개)
#  - Mob_db
#
# 수정될 RE 폴더 내 yml 파일 목록
# Item 부분 (16개)
#  - achievement_db , enchantgrade , iten_combos , item_db , item_db_equip , item_db_etc,
#  item_db_usable , item_group_db , item_reform , laphine_synthesis , laphine_upgrade,
#  pet_db , quest_db , refine , skill_db , stylist
# Monster 부분 (6개)
# - Elemental_db , mercenary_db , mob_db , mob_summon , pet_db , quest_db

# 사용할 모듈 import
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msgbox
import os

def csv_path(): # csv 경로 찾기 버튼 함수
    csv_val = filedialog.askopenfilenames(title="한글화된 csv 파일을 선택하세요", filetypes=(("csv 파일", "*.csv"), ("모든 파일", "*.*")))
    if csv_val == '': #사용자가 취소를 누를 때
        return
    # 파일을 선택했을 때
    csv_dir.delete(0, END)
    csv_dir.insert(0, csv_val)
    
def re_path(): # re 폴더 경로 찾기 버튼 함수
    re_folder_val = filedialog.askdirectory(title="db폴더내 re 폴더를 선택하세요")
    if re_folder_val == '': #사용자가 취소를 누를 때
        return
    # 파일을 선택했을 때
    re_desc.delete(0, END)
    re_desc.insert(0, re_folder_val)
    
def run_trans():
    if csv_dir.get() == '' or re_desc.get() == '': # 폴더 경로가 하나라도 비어있을경우 실행안됨
        processing_text.delete("1.0", END)
        processing_text.insert(END, "CSV 파일 또는 폴더 경로를 지정해주세요.")
    else: # 폴더 경로가 입력된 조건은 만족.
        
        if csv_var.get() == 0: # CSV 파일 타입 선택 안했을 경우
            processing_text.delete("1.0", END)
            processing_text.insert(END, "CSV 파일의 타입을 선택해주세요.")
        elif csv_var.get() == 1: # item db 일 경우
            processing_text.insert(END, "1")
        elif csv_var.get() == 2: # mob db 일 경우
            processing_text.insert(END, "2")


# Program window 설정
root = Tk()
root.title("rAthena db - Item, Monster Name Changer") # 프로그램 제목타이틀
root.geometry("670x430+300+100") # 프로그램 해상도
root.resizable(False, False) # 프로그램 크리 변경 불가

try:
    # Labels
    titlename = Label(root, text="rAthena db folder - Item, Mob Name chaner", font="arial 16 bold") # 제목 라벨
    titlename.place(x=135, y=15)
    dir_path_desc = Label(root, text="CSV 파일 선택") # CSV 파일 입력 설명 라벨
    dir_path_desc.place(x=14, y=60)
    re_desc = Label(root, text="rAthena/db/re 폴더경로 입력") # RE 폴더 입력 설명 라벨
    re_desc.place(x=14, y=145)
    makers = Label(root, text="제작자 : SerG") #제작자
    makers.place(x=574, y=378)
    blogs = Label(root, text="https://blog.naver.com/hihihi0102") #블로그주소
    blogs.place(x=460, y=398)
    # Directory Entry
    csv_dir = Entry(root, width=80) # CSV 경로 엔트리
    csv_dir.place(x=15, y=84)
    re_desc = Entry(root, width=80) # RE 폴더 경로 엔트리
    re_desc.place(x=15, y=169)
    # CSV 파일의 Item_db , Mob_db 구분용 버튼
    csv_label = Label(root, text="CSV파일 타입 선택 : ") # 라디오버튼 선택 설명 라벨
    csv_label.place(x=15, y=110)
    csv_var = IntVar() # 라디오버튼 선택을 정수형으로 저장하는 변수
    rbtn1_item = Radiobutton(root, text="Item", value=1, variable = csv_var) # 라디오버튼 1 (아이템)
    rbtn2_mob = Radiobutton(root, text="Mob(monster)", value=2, variable = csv_var) # 라디오버튼 2 (몹) 
    rbtn1_item.place(x=135, y=109)
    rbtn2_mob.place(x=190, y=109)
    # 프로세싱 과정 입력용 텍스트박스
    processing_text = Text(root, width=90, height=12, wrap='char')
    processing_text.place(x=15, y=210)
    # 찾기 및 시작버튼
    btn1_csvpath = Button(root, width=8, text="찾기", relief="raised", command=lambda: csv_path()) # CSV 파일 찾기버튼
    btn1_csvpath.place(x=590, y=80)
    btn2_repath = Button(root, width=8, text="찾기", relief="raised", command=lambda: re_path()) # 폴더 찾기 버튼
    btn2_repath.place(x=590, y=165)
    btn3_start = Button(root, width=8, text="Run", relief="raised", command=lambda: run_trans()) # 시작버튼
    btn3_start.place(x=315, y=385)


except Exception as err: #예외처리
    msgbox.showerror("에러", err)


root.mainloop()