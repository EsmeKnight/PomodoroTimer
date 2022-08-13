import math
from tkinter import *

# CONSTANTS
WORK_MINS = 25
SHORT_BREAK_MINS = 5
LONG_BREAK_MINS = 20

FONT = "courier"
GREEN_BG = "#9ED2C6"

# timer
def start_countdown():
    countdown(WORK_MINS * 60)
    countdown(SHORT_BREAK_MINS * 60)
    countdown(WORK_MINS * 60)
    countdown(SHORT_BREAK_MINS * 60)
    countdown(WORK_MINS * 60)
    countdown(SHORT_BREAK_MINS * 60)
    countdown(WORK_MINS * 60)
    countdown(SHORT_BREAK_MINS * 60)
    countdown(WORK_MINS * 60)
    countdown(LONG_BREAK_MINS * 60)


num_cycles = 0


def countdown(count):
    global num_cycles
    count_mins = math.floor(count / 60)
    count_secs = count % 60
    if count_secs < 10 and count_secs >= 0:
        count_secs = f"0{count_secs}"
    if count_mins < 10 and count_mins >= 0:
        count_mins = f"0{count_mins}"
    if count_secs == -1:
        count_secs = 59
        count_mins = count_mins - 1
    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        if num_cycles <= 5:
            num_cycles += 1
            cycles["text"] = "✔" * num_cycles


# num = 5
# def test(val):
#     if val >= 0:
#         print(val)
#         val -= 1
#         test(val)


# UI
# window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=20, pady=20, bg=GREEN_BG)
window.minsize(width=200, height=224)

# # tkinter built in wait
# window.after(1000, test, num)


# timer label
timer = Label(text="Pomodoro Timer", font=FONT, bg=GREEN_BG)
timer.grid(column=1, row=0)

# canvas (tomato image container with countdown clock)
canvas = Canvas(width=200, height=224)
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
start_button = Button(text="Start", command=start_countdown)
start_button.grid(column=0, row=2)
# number of cycles will appear in column between these buttons (directly beneath tomato)
reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2)

cycles = Label(text="", bg=GREEN_BG)
cycles.grid(column=1, row=3)

# functions as a while loop to keep window open
window.mainloop()
