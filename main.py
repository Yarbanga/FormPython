from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

Label(root, text="Python Registration Form ", font="ar 15 bold").grid(row=0, column=3)

name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergence = Label(root, text="Emergence")
paymentmood = Label(root, text="Payment Mood")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergence.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencevalue = StringVar
paymentmoodvalue = StringVar
checkvalue = IntVar

nameentry = Entry(root, textvariable =namevalue)
phoneentry = Entry(root, textvariable =phonevalue)
genderentry = Entry(root, textvariable =gendervalue)
emergenceentry = Entry(root, textvariable =emergencevalue)
paymentmoodentry = Entry(root, textvariable =paymentmoodvalue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergenceentry.grid(row=4, column=3)
paymentmoodentry.grid(row=5, column=3)


checkbtn = Checkbutton(text="remember me ?", variable= checkvalue)
checkbtn.grid(row=6, column= 3)

Button(text="Submit", command=getvals).grid(row=7, column=3)


root.mainloop()