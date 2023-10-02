from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Comic Sans"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(my_timer)
    timer.config(text="Timer", fg="#ffffff")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        timer.config(text="Long break", fg=RED)
    elif reps % 2 == 1:
        count_down(work)
        timer.config(text="Work", fg=GREEN)
    else:
        count_down(short_break)
        timer.config(text="Short break", fg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    global reps
    count_min = floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    elif count < 0:
        start_timer()
        if reps % 2 == 0:
            checkmarks = floor(reps/2)*"✔"
            check.config(text=checkmarks)

# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("Rosie")
window.config(padx=100, pady=50, bg=PINK)

# canvas
canvas = Canvas(width=200, height=223, bg=PINK, highlightthickness=0)
imagine = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=imagine)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

# lable sus si label status
timer = Label(text="Timer", fg="#ffffff", bg=PINK, font=(FONT_NAME, 30, "bold"))
timer.grid(row=0, column=1)

# checkmark
check = Label(fg=GREEN, bg=PINK, font=(FONT_NAME, 16, "bold"))
check.grid(row=3, column=1)

# buton start si reset
start = Button(text="Start", bg=PINK, font=(FONT_NAME, 12, "bold"), command=start_timer)
start.grid(row=2, column=0)
reset = Button(text="Reset", bg=PINK, font=(FONT_NAME, 12, "bold"), command=reset_timer)
reset.grid(row=2, column=2)


window.mainloop()
