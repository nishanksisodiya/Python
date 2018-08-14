import tkinter as tk
import tkinter.messagebox as mb
win=tk.Tk()
win.geometry("100x200")
s=tk.Scrollbar(win)
s.pack(side="right", fill="y")
T=tk.Text(win,font=("Social Logos",30))
T.pack()
for i in range(65,92):
    T.insert(tk.END,chr(i)+"\n")
for i in range(97,123):
    T.insert(tk.END,chr(i)+"\n")
s.config(command=T.yview)
tk.mainloop()
