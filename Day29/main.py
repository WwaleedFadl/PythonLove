from tkinter import *
            
# ---------------------------- UI SETUP ------------------------------- #
# ------------------------------------- Window
window = Tk()
window.title("Password Generator")
window.config(padx=100,pady=50,bg=YELLOW)
# -------------------------------------  Label Timer
timer_label = Label(text="Mypass", font=("Arial", 50),fg=GREEN,bg=YELLOW)
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
