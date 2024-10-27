

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer=None


from tkinter import *
import math

#from time import time
#count_down(5)
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps=0
    canvas.itemconfig(timer_text, text= "00:00")
    check_mark.config(text="")
    title_label.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #
# change 5 to needed term
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN*60
    #work_sec=6
    short_break_sec = SHORT_BREAK_MIN*60
    #short_break_sec = 10
    long_break_sec = LONG_BREAK_MIN*60
    if reps % 8==0:
        title_label.config(text="Long Break", fg=PINK)
        count_down(long_break_sec)
    elif reps % 2==0:
        title_label.config(text="Short Break",fg=GREEN)
        count_down(short_break_sec)
    else:
        title_label.config(text="Work", fg=RED)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec <10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark =""
        work_sessions=math.floor(reps/2)
        for _ in range (work_sessions):
            mark+="V"
        check_mark.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Image Tomato

canvas = Canvas(width=210, height=234, bg=YELLOW, highlightthickness=0)
image_tomato = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=image_tomato)
#Timer_Label

timer_text = canvas.create_text(103,130,text = "00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)
#Label
title_label= Label(fg= GREEN, text = "Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW)
#title_label
title_label.grid(column=1,row=0)


#Button1
start_button = Button(fg="black", text = "Start", font= (FONT_NAME, 12, ), command=start_timer)
start_button.grid(column=0, row=2)

#Button2
reset_button = Button(fg="black", text = "Reset", font= (FONT_NAME, 12), command=reset_timer)
reset_button.grid(column=2, row=2)

#Text
check_mark = Label(fg = GREEN, font= (FONT_NAME, 20, "bold"), bg = YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()
