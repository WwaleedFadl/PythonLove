from tkinter import *
def miles_to_km(): 
    miles = input1.get()
    km = float(miles) * 1.609
    input2.config(text=km)

#######################################################################
window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)


###################################ROW 0#####################################
my_label = Label(text="Miles", font=("Arial", 24))
my_label.grid(column=3,row=0)


#entry 
input1 = Entry(width=30)
input1.grid(column=2,row=0)


###################################ROW 1#####################################


my_label2 = Label(text="Is equal to", font=("Arial", 24))
my_label2.grid(column=1,row=1)


#entry 
#input2 = 0)
input2= Label(text="0", font=("Arial", 24))
input2.grid(column=2,row=1)


# label
my_label3 = Label(text="KM", font=("Arial", 24))
my_label3.grid(column=3,row=1)


###################################ROW 2#####################################


#button 
button = Button(text='Calculate',command=miles_to_km)
button.grid(column=2,row=2)


#######################################################################
window.mainloop()
