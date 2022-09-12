# 2번 프로그램
# 해당 프로그램은, 구버젼 서버파일에서 한글화된 db 파일을 사용하여
# ID , 영문AegisName , 영문ItemName , 한글AegisName , 한글ItemName 양식의 CSV 파일을 만들어주는 프로그램임.

# 해당 프로그램으로 만들어진 CSV 파일을 바탕으로,
# 이 다음 프로그램에서 rAthena/db/re 폴더 내
# item_db 와 mob_db가 참조되는 모든 yml 파일의 명칭을
# 영문AegisName -> 한글AegisName
# 영문ItemName -> 한글ItemName 으로 바꿔줌.

# 주의
# Input 되는 구버젼 한글 db 파일은 확장자를 txt -> csv 로 변경 후
# 엑셀에서 ID, AegisName, ItemName 열만 남기고 다른 데이터는 삭제후
# 넣어줘야 함

from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msgbox
from csv_insert_func import insert_korean

root = Tk()
root.title("CSV input korean Name") # 프로그램 제목타이틀
root.geometry("670x230+300+100") # 프로그램 해상도
root.resizable(False, False) # 프로그램 크리 변경 불가

def txt_path():
    txt_dir = filedialog.askopenfilenames(title="한글화된 csv 파일을 선택하세요", filetypes=(("csv 파일", "*.csv"), ("모든 파일", "*.*")))
    if txt_dir == '': #사용자가 취소를 누를 때
        return
    
    # 파일을 선택했을 때
    txt_db_dir.delete(0, END)
    txt_db_dir.insert(0, txt_dir)
    
def csv_path():
    csv_dir = filedialog.askopenfilenames(title="csv 파일을 선택하세요", filetypes=(("csv 파일", "*.csv"), ("모든 파일", "*.*")))
    if csv_dir == '': #사용자가 취소를 누를 때
        return
    
    # 파일을 선택했을 때
    ex_csv_dir.delete(0, END)
    ex_csv_dir.insert(0, csv_dir)

try:
    # 타이틀, 제작자, 블로그, 입력설명
    titlename = Label(root, text="Insert Korean Name at extracted CSV", font="arial 16 bold") #제목
    titlename.place(x=160, y=15)
    makers = Label(root, text="제작자 : SerG") #제작자
    makers.place(x=10, y=180)
    blogs = Label(root, text="https://blog.naver.com/hihihi0102") #블로그주소
    blogs.place(x=10, y=200)
    dir_path_desc = Label(root, text="이전 한글화된 db csv 파일 선택") #입력창설명
    dir_path_desc.place(x=14, y=60)
    ex_csv = Label(root, text="추출한 CSV 파일 선택") #입력창설명
    ex_csv.place(x=14, y=110)

    # txt 파일 경로
    txt_db_dir = Entry(root, width=80)
    txt_db_dir.place(x=15, y=84)
    
    # CSV 파일 경로
    ex_csv_dir = Entry(root, width=80)
    ex_csv_dir.place(x=15, y=134)

    # txt 찾기 버튼
    btn1_txtpath = Button(root, width=8, text="찾기", relief="raised", command=txt_path)
    btn1_txtpath.place(x=590, y=80)
    
    # csv 찾기 버튼
    btn2_csvpath = Button(root, width=8, text="찾기", relief="raised", command=csv_path)
    btn2_csvpath.place(x=590, y=130)

    # 시작버튼
    btn3_start = Button(root, width=10, text="시작", relief="raised", command=lambda:insert_korean(txt_db_dir.get(), ex_csv_dir.get()))
    btn3_start.place(x=300, y=185)

except Exception as err: #예외처리
    msgbox.showerror("에러", err)

root.mainloop()