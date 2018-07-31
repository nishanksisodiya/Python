from tkinter import *
root=Tk()
Label(root, text="First Name",font="TapingYourHand 20").grid(row=0,column=0)
Label(root, text="Last Name",font="TapingYourHand 20").grid(row=0,column=3)
e1=Entry(root)
e2=Entry(root)
e1.grid(row=0,column=1)
e2.grid(row=0,column=4)
mainloop()
