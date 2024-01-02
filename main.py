from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        # if it's the 2nd/4th/6th rep:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)

    else:
        # if it's the 1st/3rd/5th/7th rep:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_sec == 0:
        count_sec = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # to reconfigure the canvas item
    if count > 0:
        global timer
        timer = window.after(1000, count_down,
                             count - 1)  # .after function , it takes the amount of time in ms , function , *agrs
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

# Add label into application
title_label = Label(text="Timer", foreground=GREEN, font=(FONT_NAME, 50), background=YELLOW)
title_label.grid(column=1, row=0)

# Creating canvas to display the image on application
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")  # file path
canvas.create_image(100, 112, image=tomato)  # image creation
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))  # text creation on canva over the image
canvas.grid(row=1, column=1)

# Buttons
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)
Reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
Reset.grid(column=2, row=2)

# Add Check Mark
check_marks = Label(foreground=GREEN, background=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
