from tkinter import *
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=100,pady=50)

# ------------------------------------- Canvas
canvas = Canvas(width=200,height=200,highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

# -------------------------------------  Label Website
website_label = Label(text="Website", font=("Arial", 10))
website_label.grid(column=0,row=1)
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)

################
email_username_label = Label(text="Email / Username", font=("Arial", 10))
email_username_label.grid(column=0,row=2)
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)

################
password_label = Label(text="Password", font=("Arial", 10))
password_label.grid(column=0,row=3)
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)
generate_password_button = Button(text='Generate Password',highlightthickness=0)
generate_password_button.grid(column=3,row=3)

#######################################################
add_button = Button(text='Add',highlightthickness=0)
add_button.grid(column=1,row=4,columnspan=2)

#--------------------------------------------- 
window.mainloop()
