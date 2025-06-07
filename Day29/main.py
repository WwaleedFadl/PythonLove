from tkinter import *
from tkinter import messagebox
import random
import pyperclip


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list) 
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=100,pady=50)
######################################## Functions 

def save(): 
    website_value = website_entry.get() 
    email_value = email_entry.get() 
    password_value = password_entry.get() 

    if (len(website_value) == 0 or len(password_value) == 0 or len(email_value) == 0):
        messagebox.showinfo(title="Error",message="Please do not leave any of the previous entries empty.");

    else: 
        is_ok=messagebox.askokcancel(title=website_value,message=f"These are the details entered: \n Email: {email_value}\n password: {password_value} \n is it ok to save ? ")

        if is_ok: 
             with open("info.txt",'a') as data_file: 
                  data_file.write(f"{website_value} | {email_value} | {password_value}")
                  data_file.write('\n')
                  website_entry.delete(0,END)
                  email_entry.delete(0,END)
                  password_entry.delete(0,END)

# ------------------------------------- Canvas ------------------------------------
canvas = Canvas(width=200,height=200,highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

# -------------------------------------  Label Website -----------------------------
website_label = Label(text="Website", font=("Arial", 10))
website_label.grid(column=0,row=1)
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

#######################################################################################
email_username_label = Label(text="Email / Username", font=("Arial", 10))
email_username_label.grid(column=0,row=2)
email_entry = Entry(width=35)
email_entry.insert(0,"wwaleedFadl@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2)

################
password_label = Label(text="Password", font=("Arial", 10))
password_label.grid(column=0,row=3)
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

generate_password_button = Button(text='Generate Password',highlightthickness=0,command=generate_password)
generate_password_button.grid(column=3,row=3)

#######################################################
add_button = Button(text='Add',highlightthickness=0,command=save)
add_button.grid(column=1,row=4,columnspan=2)

#--------------------------------------------- 
window.mainloop()
