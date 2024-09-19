from tkinter import *
import math
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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    label_mark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
# Start Button Widget


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        # 1/3/5/7
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        # 8
        count_down(long_break_sec)
        label.config(text="Long Break", fg=RED)
    else:
        # 2/4/6
        count_down(short_break_sec)
        label.config(text="Short Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# With GUIs, TKinter, we cannot use a "while loop". Otherwise, the window.mainloop() won't run and
# nothing will appear on screen.


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # To change a canvas is different from changing a label, we must use .itemconfig, instead of such .config
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        # After 1000 milliseconds (1 sec) window.after will call the function count_down, with the input of count - 1
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
            label_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# The png tomato image has: 200x223
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# Now we have to insert the image using the method create_image
# create_image only accepts images that are processed through PhotoImage() class
tomato_img = PhotoImage(file="tomato.png")

# The first value is where the image will be centered in X and the second is where it is centered on the y
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# calls action() when pressed
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)


# Reset Button Widget
def action():
    print("Do something")


# calls action() when pressed
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

# Check Mark Label
label_mark = Label(text="✔", fg=GREEN, bg=YELLOW)
label_mark.grid(column=1, row=3)

# Timer Label
label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
label.grid(column=1, row=0)


window.mainloop()
