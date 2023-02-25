# importing necessary modules
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

# Setting the colours and font name for the UI
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# Setting the durations for work, short break, and long break in minutes
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """A function to reset the timer and clear the checkmarks"""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN)
    label_checkmark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """A function to start the timer and change the label text and color according to the current session"""
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label.config(text="Break", fg=RED)
    elif reps % 2 != 0:
        count_down(WORK_MIN * 60)
        label.config(text="Work", fg=GREEN)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """A function to implement the countdown timer and display the remaining time on the canvas"""
    count_min = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            mark += "✓"
        label_checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
# Initializing the tkinter window
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=210, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=tomato_img)
timer_text = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)

# Timer label
label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'normal'))
label.grid(column=1, row=0)

# Start and Reset Buttons
start_btn = Button(text="Start", borderwidth=0, highlightthickness=0, pady=2, padx=2, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, borderwidth=0, border=0, pady=2, padx=2, command=reset_timer)
reset_btn.grid(column=2, row=2)
reset_btn.config(relief="solid")

# Checkmark label
label_checkmark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, 'normal'))
label_checkmark.grid(column=1, row=3)

window.mainloop()
