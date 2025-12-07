
import sudoku_solver
from tkinter import *
import copy

class button_sort:
    def table(self, interface, board, input_row, mode_func):
        global current_light_num
        current_light_num=[[]for i in range(10)]
        current_light_num[0].append(0)
        self.buttons = [[None for _ in range(9)] for _ in range(9)]

        for rdx, row in enumerate(board):
            for cdx, data in enumerate(row):
                # 3x3 구분
                crdx = 8 - rdx
                tmp = rdx//3 + cdx//3
                if (tmp%2==0):
                    back_color = 'white'
                else:
                    back_color = 'lightgray'
                if (mode_func==sudoku_solver.is_current_cross_board_valid and (rdx==cdx or crdx==cdx)):
                    back_color = 'lightgreen'
                if (data=="#"): 
                    data=" "
                    btn = Button(interface, text=data, width=6, height=2, bg=back_color, font="bold", command=lambda rdx=rdx, cdx=cdx: button_input(rdx, cdx, mode_func))
                else: 
                    btn = Button(interface, text=data, width=6, height=2, bg=back_color, font="bold", fg="blue")
                    num = int(data)
                    current_light_num[num].append((rdx, cdx, back_color))
                    CLN = len(current_light_num[num])
                    if(CLN==9):
                        num_buttons[num].config(bg="lightgray")
                btn.grid(row=rdx+input_row, column=cdx)
                self.buttons[rdx][cdx] = btn
    
def button_search_num(num):
    global current_light_num, num_buttons
    if(current_light_num[0][0]!=0):
        tmp = current_light_num[0][0]
        for (rdx, cdx, back_color) in current_light_num[tmp]:
            cal_ref.buttons[rdx][cdx].config(bg=back_color)
        num_buttons[tmp].config(bg=num_buttons[0])
        if(current_light_num[0][0]==num or num==0):
            current_light_num[0][0]=0
            return
    if(num!=0):
        for (rdx, cdx, back_color) in current_light_num[num]:
            cal_ref.buttons[rdx][cdx].config(bg="yellow")
        num_buttons[0] = num_buttons[num].cget("bg")
        num_buttons[num].config(bg="yellow")
        current_light_num[0][0]=num

def search_del(rdx, cdx):
    for num in range(1,10):
        for idx, (r, c, back_color) in enumerate(current_light_num[num]):
            if(r==rdx and c==cdx):
                cal_ref.buttons[r][c].config(bg=back_color)
                del current_light_num[num][idx]
                CLN = len(current_light_num[num])
                if(CLN!=9 and current_light_num[0][0]!=num):
                    num_buttons[num].config(bg="white")
                elif(CLN!=9):
                    num_buttons[0] = "white"
                return
            
def button_input(rdx, cdx, mode_func):
    global current_input, current_inter
    if(current_input==1): current_inter.destroy()
    interface_input = Toplevel()
    current_inter = interface_input
    tk = interface_input
    tk.title("input")

    for i in range(1,10):
        btn = Button(tk, text=str(i), width=6, height=2, font="bold", command=lambda i=i: button_change(tk, rdx, cdx, i, mode_func))
        btn.grid(row=(i-1)//3, column=(i-1)%3)  
    btn = Button(tk, text=" ", width=6, height=2, font="bold", command=lambda: button_change(tk, rdx, cdx, "#", mode_func))
    btn.grid(row=4, column=1)
    current_input = 1

def button_change(tk, rdx, cdx, i, mode_func):
    global board_ref, current_input
    tmp = board_ref[rdx][cdx]
    board_ref[rdx][cdx] = str(i)
    # GUI 버튼 변경
    if(mode_func(board_ref)):
        if(i=="#"): i=" "
        search_del(rdx, cdx)
        cal_ref.buttons[rdx][cdx].config(text=str(i), fg="black")
        if(i!=" "):
            num=int(i)
            back_color = cal_ref.buttons[rdx][cdx].cget("bg")
            current_light_num[num].append((rdx, cdx, back_color))
            CLN = len(current_light_num[num])
            if(num==current_light_num[0][0]):
                cal_ref.buttons[rdx][cdx].config(bg="yellow")
                if(CLN==9):
                    num_buttons[0] = "lightgray"
            elif(CLN==9):
                num_buttons[num].config(bg="lightgray")
            count = 0
            for numa in range(1, 10):
                CLN = len(current_light_num[numa])
                if(CLN==9):
                    count+=1
            if(count==9):
                instant = Toplevel()
                instant.title("완성")
                text = Label(instant, height=2, text="스도쿠 완성!!", font=("bold", 30))
                text.grid(row=0, column=0, columnspan= 2)
                rego = Button(instant, text="돌아가기", width=8, height=2, font="bold", command=lambda: button_rego(instant))
                rego.grid(row=2, column=0)
                ex = Button(instant, text="종료", width=8, height=2, font="bold", command=lambda: button_ex(instant))
                ex.grid(row=2, column=1)
    else:
        instant = Toplevel()
        instant.title("Error")
        text = Label(instant, text="wrong answer")
        text.grid()
        instant.after(3000, instant.destroy)
        board_ref[rdx][cdx] = tmp
    # 팝업 닫기
    if tk is not None:
        current_input = 0
        tk.destroy()

def button_rego(instant):
    instant.destroy()

def button_ex(instant):
    if sudoku_main:
        sudoku_main()
    instant.destroy()
    interface.destroy()

def button_reset():
    global board_init, board_ref
    board_ref = copy.deepcopy(board_init)
    num_tmp = current_light_num[0][0]
    button_search_num(0)
    for r in range(9):
        for c in range(9):
            tmp = board_ref[r][c]
            if(tmp=="#"): 
                tmp=" "
                cal_ref.buttons[r][c].config(text=tmp)
                search_del(r, c)
    button_search_num(num_tmp)

def button_judge(mode_func):
    board_ans = copy.deepcopy(board_init)
    sudoku_solver.solve_sudoku(board_ans, mode_func)
    for r in range(9):
        for c in range(9):
            init = board_init[r][c]
            tmp = board_ref[r][c]
            answer = board_ans[r][c]
            if(tmp!="#" and tmp!=answer):
                cal_ref.buttons[r][c].config(fg="red")
            elif(answer!=init):
                cal_ref.buttons[r][c].config(fg="black")

def button_del(mode_func):
    board_ans = copy.deepcopy(board_init)
    sudoku_solver.solve_sudoku(board_ans, mode_func)
    num_tmp = current_light_num[0][0]
    button_search_num(0)
    for r in range(9):
        for c in range(9):
            tmp = board_ref[r][c]
            answer = board_ans[r][c]
            if(tmp!="#" and tmp!=answer):
                button_change(None, r, c, "#", mode_func)
                search_del(r, c)
                back_color = cal_ref.buttons[r][c].cget("bg")
                cal_ref.buttons[r][c].config(bg="red")
                cal_ref.buttons[r][c].after(1000, lambda r=r, c=c, back_color=back_color : cal_ref.buttons[r][c].config(bg=back_color))

    button_search_num(num_tmp)

def button_answer(mode_func):
    global board_init, board_ref
    board_tmp = copy.deepcopy(board_ref)
    board_ref = copy.deepcopy(board_init)
    sudoku_solver.solve_sudoku(board_ref, mode_func)
    num_tmp = current_light_num[0][0]
    button_search_num(0)
    for r in range(9):
        for c in range(9):
            tmp = board_tmp[r][c]
            answer = board_ref[r][c]
            numa = int(answer)
            BK = cal_ref.buttons[r][c].cget("bg")   
            cal_ref.buttons[r][c].config(text=answer)
            if(tmp!="#" and tmp!=answer):
                cal_ref.buttons[r][c].config(fg="red")
                search_del(r, c)
            elif(tmp=="#"):
                cal_ref.buttons[r][c].config(fg="black")
            if(tmp!=answer):
                current_light_num[numa].append((r, c, BK))
                CLN = len(current_light_num[numa])
                if(CLN==9):
                    num_buttons[numa].config(bg="lightgray")
    button_search_num(num_tmp)



def run_sudoku(board, mode, level, on_close=None):
    global board_ref, cal_ref, board_init, current_input, num_buttons, interface, sudoku_main
    sudoku_main = on_close
    if mode=='original':
        mode_func = sudoku_solver.is_current_board_valid
    elif mode=='cross':
        mode_func = sudoku_solver.is_current_cross_board_valid
    current_input = 0
    board_init = copy.deepcopy(board)
    board_ref = copy.deepcopy(board_init)
    interface = Tk()
    interface.title(mode)
    title = Label(interface, height=3, text=level, font=("bold", 14))
    title.grid(row=0, column=4)
    reset = Button(interface, text="리셋", width=6, height=2, command=button_reset)
    reset.grid(row=0, column=0)
    answer = Button(interface, text="정답", width=6, height=2, command=lambda: button_answer(mode_func))
    answer.grid(row=0, column=2)
    judge = Button(interface, text="점검", width=6, height=2, command=lambda: button_judge(mode_func))
    judge.grid(row=0, column=7)
    Bdel = Button(interface, text="삭제", width=6, height=2, command=lambda: button_del(mode_func))
    Bdel.grid(row=0, column=8)
    #라벨들...
    lbl = Label(interface)
    lbl.grid(row=12)
    labels = [i for i in range(1,10)]
    num_buttons = [() for i in range(10)]
    for idx, num in enumerate(labels):
        btn = Button(interface, text=num, width=6, height=2, bg="white", font="bold", command=lambda num=num: button_search_num(num))
        btn.grid(row=13, column=idx)
        num_buttons[num] = btn

    cal = button_sort()
    cal_ref = cal
    cal.table(interface, board, 3, mode_func)

    interface.mainloop()

