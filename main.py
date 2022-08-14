from cgitb import text
import math
from tkinter import *
import time
from turtle import color, width

# CONSTANTS
WORK_MINS = 25
SHORT_BREAK_MINS = 5
LONG_BREAK_MINS = 20

FONT = "courier"
GREEN_BG = "#9ED2C6"
RED = "#FF5D5D"
L_YELLOW = "#FFF8BC"
D_YELLOW = "#FAD9A1"

CLOCK = None


# timer
num_cycles = 0


def stop_countdown():
    global num_cycles
    num_cycles = 0
    cycles.config(text="", fg=RED)
    session_title.config(text="Pomodoro Timer", fg="black")
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(
        CLOCK
    )  # must tap into CLOCK because that is what is called by the window


def start_countdown():
    global num_cycles
    num_cycles += 1

    work_secs = WORK_MINS * 60
    short_break_secs = SHORT_BREAK_MINS * 60
    long_break_secs = LONG_BREAK_MINS * 60

    # if num cycles is equal to 2 or 4 can be written as:
    if num_cycles % 2 == 0:
        countdown(short_break_secs)
        session_title.config(text="Short break", fg=L_YELLOW)
    # if num cycles is 5
    elif num_cycles % 5 == 0:
        countdown(long_break_secs)
        session_title.config(text="Long break", fg=D_YELLOW)
    # if neither of those is true then it must be a working session
    else:
        countdown(work_secs)
        session_title.config(text="Working Session", fg=RED)
    checks = ""
    for _ in range(math.floor(num_cycles / 2)):
        checks += "✔"
    cycles.config(text=checks, fg=RED)


def countdown(count):
    count_mins = math.floor(count / 60)
    count_secs = count % 60
    if count_secs < 10:
        count_secs = f"0{count_secs}"
    if count_mins < 10 and count_mins >= 0:
        count_mins = f"0{count_mins}"
    if count_secs == -1:
        count_secs = 59
        count_mins = count_mins - 1
    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")
    if count > 0:
        global CLOCK
        CLOCK = window.after(1000, countdown, count - 1)


# UI
# window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=20, pady=20, bg=GREEN_BG)
# make window start at size == working session window size
window.geometry("350x325")
window.minsize(width=200, height=224)

# frame for window
frame = Frame(window, bg=GREEN_BG)
frame.place(relx=0.5, rely=0.5, anchor="c")

# session_title label
session_title = Label(
    frame, text="Pomodoro Timer", font=(FONT, 20, "bold"), bg=GREEN_BG
)
session_title.grid(column=1, row=0)

# canvas (tomato image container with countdown CLOCK)
canvas = Canvas(frame, width=200, height=224)
canvas.configure(bg=GREEN_BG, highlightthickness=0)  # highlight here is the boarder
tomato_img = PhotoImage(file="Pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    103,
    120,
    text="00:00",
    fill="white",
    font=(FONT, 25, "bold"),
)
canvas.grid(column=1, row=1)

# buttons
start_button = Button(frame, text="Start", command=start_countdown)
start_button.grid(column=0, row=2)
# number of cycles will appear in column between these buttons (directly beneath tomato)
reset_button = Button(frame, text="Reset", command=stop_countdown)
reset_button.grid(column=2, row=2)

cycles = Label(frame, text="", bg=GREEN_BG)
cycles.grid(column=1, row=3)

# functions as a while loop to keep window open
window.mainloop()
