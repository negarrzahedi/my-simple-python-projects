import tkinter as tk
import random
from tkinter import messagebox


root=tk.Tk()
root.geometry("400x350")
root.title("تولید رمز عبور")



var=tk.IntVar()
var2=tk.BooleanVar(value=True)

def leng():
        if en_length <4:
            messagebox.showerror("the pass length should be more than 4")


label_length=tk.Label(root , text="password length : ",font=("Tahoma" ,12))
label_length.pack(padx=10 , pady=10)

en_length=tk.Entry(root , text="push" ,font=("Tahoma" ,12),textvariable=var)
en_length.pack(padx=10 , pady=10)

def tick():
     if check or check2 or check3 :
          pass
     else:
          messagebox.showerror("you should selecte one or more")

check=tk.Checkbutton(root,text="حروف کوچک",variable=var2)
check.pack(padx=10 , pady=10)

check2=tk.Checkbutton(root,text="حروف بزرگ",variable=var2)
check2.pack(padx=10 , pady=10)

check3=tk.Checkbutton(root,text="اعداد",variable=var2)
check3.pack(padx=10 , pady=10)


def password():
    toolramz=int(en_length.get())
    en_pass.config(text=random.choice())



button=tk.Button(root,text="تولید رمز" ,font=("Tahoma" ,12) , command=password)
button.pack(pady=10 ,padx=10)


en_pass=tk.Entry(root , text="",font=("Tahoma" ,12),textvariable=var)
en_pass.pack(pady=10 ,padx=10)







root.mainloop()
