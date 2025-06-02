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
    timer_label.config(text="My Pomodoro", font=("Arial", 50),fg=GREEN,bg=YELLOW)
    canvas.itemconfig(timer_text,text="00:00") 
    Done_label.config(text='')
    global reps 
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps 
    reps += 1
    work_sec = WORK_MIN * 60 
    short_break_sec = SHORT_BREAK_MIN * 60 
    long_break_sec = LONG_BREAK_MIN * 60  
    if reps % 8 == 0 : 
        count_down(long_break_sec)
        timer_label.config(text="Enjoy your long break your deserve it", font=("Arial", 50),fg=GREEN,bg=YELLOW)
    elif reps %2 ==0: 
        count_down(short_break_sec)
        timer_label.config(text="5 min break", font=("Arial", 50),fg=GREEN,bg=YELLOW)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", font=("Arial", 50),fg=RED,bg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    #00:00
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10: 
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0: 
        global timer
        timer = window.after(1000,count_down,count - 1)
    else: 
        start_timer()
        mark = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += '✔'
        Done_label.config(text=mark)

            
# ---------------------------- UI SETUP ------------------------------- #
# ------------------------------------- Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


# -------------------------------------  Label Timer
timer_label = Label(text="My Pomodoro", font=("Arial", 50),fg=GREEN,bg=YELLOW)
timer_label.grid(column=1,row=0)

# ------------------------------------- Canvas
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,'bold'))
canvas.grid(column=1,row=1)

#-------------------------------------  Count Down
#count_down(5)

# -------------------------------------  Button Marker True  Button 
# Start Button 
button_start = Button(text='Start',highlightthickness=0,command=start_timer)
button_start.grid(column=0,row=2)

# End Button 
button_end = Button(text='Reset',highlightthickness=0,command=reset_timer)
button_end.grid(column=2,row=2)

#Done Label
Done_label = Label(font=("Arial", 50),fg=GREEN,bg=YELLOW)
Done_label.grid(column=1,row=3)


#--------------------------------------------- 
window.mainloop()
