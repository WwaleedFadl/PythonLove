from tkinter import *

def button_clicked(): 
    input_value = input.get()
    my_label['text'] =input_value 

#######################################################################

window = Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)
window.config(padx=100,pady=200)


# label
my_label = Label(text="I am just a label 😨", font=("Arial", 24))
my_label.grid(column=0,row=0)
my_label.config(padx=50,pady=50)


#button 
button = Button(text='Click me',command=button_clicked)
button.grid(column=1,row=1)


#button 
button1 = Button(text='Click me',command=button_clicked)
button1.grid(column=3,row=0)


#entry 
input = Entry(width=30)
input.grid(column=2,row=2)


#######################################################################
window.mainloop()
