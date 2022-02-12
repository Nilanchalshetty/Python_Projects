from tkinter import *
import random
root=Tk()
root.title("Dice Simulator")
root.geometry("600x500")
lable=Label(root,font=("Times New Roman",300,'bold'),text="",fg='blue')
def rolldice():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    lable.configure(text=f'{random.choice(dice)}')
    lable.pack()

button=Button(root,font=("Timr New Roman",25,'bold'),text="Dice Roll",command=rolldice,bg='yellow',fg='red')
button.pack()
root.mainloop()