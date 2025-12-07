import threading
import sudoku_inter
import sudoku_board
#from tkinter import *

def sudoku(mode, level, loading_win):
    board = sudoku_board.make_random(mode, level)
    # 로딩창 닫기
    loading_win.destroy()
    # 메인스레드에서 GUI 변경: after로 위임
    # 게임 시작 (on_close 콜백을 넘겨서 게임 종료 시 메인 윈도우 복원)
    loading_win.after(0, lambda: sudoku_inter.run_sudoku(board, mode, level, on_close=lambda: interface.deiconify()))

def start_sudoku_in_thread(mode, level, loading_win):
    t = threading.Thread(target=sudoku, args=(mode, level, loading_win), daemon=True)
    t.start()

def button_mode(num):
    global mode
    interface.withdraw()
    if(num==1):
        mode = "original"
        txt="오리지널"
    else:
        mode = "cross"
        txt="크로스"
    instant = sudoku_inter.Toplevel()
    text = sudoku_inter.Label(instant, height=2, text=txt+"의 난이도를 선택하십시오", font=("bold", 30))
    text.grid(row=1, columnspan= 3)
    easy = sudoku_inter.Button(instant, text="쉬움", width=8, height=2, font="bold", command=lambda: button_lev(instant, 1))
    easy.grid(row=3, column=0)
    nom = sudoku_inter.Button(instant, text="보통", width=8, height=2, font="bold", command=lambda: button_lev(instant, 2))
    nom.grid(row=3, column=1)
    hard = sudoku_inter.Button(instant, text="어려움", width=8, height=2, font="bold", command=lambda: button_lev(instant, 3))
    hard.grid(row=3, column=2)

def button_lev(inter, num):
    global level
    if(num==1):
        level = "easy"
    elif(num==2):
        level = "normal"
    else:
        level = "hard"
    inter.destroy()
    tmp_inter = sudoku_inter.Toplevel()
    tmp_inter.title("로딩중")
    title = sudoku_inter.Label(tmp_inter, height=3, text="로딩중...", font=("bold", 40))
    title.grid(row=0)
    tmp_inter.update()
    start_sudoku_in_thread(mode, level, tmp_inter)

def button_ex():
    interface.destroy()

if __name__ == "__main__":
    #global interface
    interface = sudoku_inter.Tk()
    interface.title("스도쿠")
    title = sudoku_inter.Label(interface, height=3, text="스도쿠", font=("bold", 60))
    title.grid(row=0, columnspan=3)
    ex = sudoku_inter.Button(interface, text="종료", width=8, height=2, font="bold", command=lambda: button_ex())
    ex.grid(row=0, column=2, columnspan=2)
    text = sudoku_inter.Label(interface, height=2, text="모드를 선택하십시오", font=("bold", 30))
    text.grid(row=1, columnspan= 3)
    ori = sudoku_inter.Button(interface, text="오리지널", width=8, height=2, font="bold", command=lambda: button_mode(1))
    ori.grid(row=3, column=0, columnspan=2)
    origin_mode = sudoku_inter.Label(interface, height=2, text=": 평범한 스도쿠입니다", font=("bold", 20))
    origin_mode.grid(row=3, column=1, columnspan=2)
    cro = sudoku_inter.Button(interface, text="크로스", width=8, height=2, font="bold", command=lambda: button_mode(2))
    cro.grid(row=4, column=0)
    cross_mode = sudoku_inter.Label(interface, height=2, text=": 대각선도 스도쿠 규칙을 지켜야 합니다", font=("bold", 25))
    cross_mode.grid(row=4, column=1, columnspan=2)
    interface.mainloop()

