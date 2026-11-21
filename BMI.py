import tkinter as tk 

root=tk.Tk()
root.geometry("700x550")
root.configure(bg="#100C2B")
root.resizable(False,False)
root.title("BMI")

def BMI(*args):
    try:
        var1=inti1.get()
        var2=inti2.get()
        lb3=tk.Label(fr2 , text=" " , font=("Tahoma" , 14),bg="#1B1543",fg="#FFFFFF" )
        lb3.pack(padx=10 , pady=10)
        if var1 <= 0 or var2 <= 0:
            lb3.config(text="قد و وزن باید مثبت باشند")
            return

        bmi=(var2/(var1*var1))*10000

        canvas.itemconfig(b,text=f"{bmi:.2f}")

        if bmi<18.5:
            lb8.config(text="کمبود وزن")

        elif 18.5<bmi< 25:
            lb8.config(text="نرمال")

        elif 25<bmi< 30:
            lb8.config(text="اضافه وزن")

        elif 30<bmi:
            lb8.config(text="چاقی")        



    except ValueError:
        lb3.config(text="لطفاً قد و وزن معتبر وارد کنید")







inti1=tk.IntVar()
inti1.trace("w" , BMI)

inti2=tk.IntVar()
inti2.trace("w" , BMI)




lb4=tk.Label(root , text="BMI calculator" , font=("Tahoma" , 14,"bold") ,fg="#FFFFFF" ,bg="#100C2B")
lb4.pack(padx=10 ,pady=10,anchor='e')
lb5=tk.Label(root , text=" شاخص توده بدنی خود را محاسبه کنید" , font=("Tahoma" , 12) ,fg="#FFFFFF",bg="#100C2B")
lb5.pack(padx=10 , pady=10,anchor='e')

fr1=tk.Frame(root,bg="#1B1543",width=260,height=330)
fr1.pack(pady=10,padx=30,side='right')
fr1.propagate(False)


lb6=tk.Label(fr1 , text="اطلاعات شما" , font=("Tahoma" , 14),fg="#FFFFFF" ,bg="#1B1543")
lb6.pack(padx=10 , pady=10,anchor='e' )
lb1=tk.Label(fr1 , text=":قد خود را وارد کنید" , font=("Tahoma" , 12),fg="#C2BDBD" ,bg="#1B1543")
lb1.pack(padx=10 , pady=10 ,anchor='e')
en1=tk.Entry(fr1 , width=30, textvariable=inti1)
en1.pack(padx=10 , pady=10,anchor='e')
lb2=tk.Label(fr1 , text=":وزن خود را وارد کنید" , font=("Tahoma" , 12),fg="#C2BDBD" ,bg="#1B1543")
lb2.pack(padx=10 , pady=10,anchor='e')
en2=tk.Entry(fr1 , width=30 , textvariable=inti2)
en2.pack(padx=10 , pady=10,anchor='e')

btn=tk.Button(fr1,text=" BMI محاسبه" ,font=("Tahoma" , 12),command=BMI,fg="#000000",bg="#B58357")
btn.pack(padx=10,pady=10)
btn.propagate(False)

def clean():
    inti1.set(0)
    inti2.set(0)
    canvas.itemconfig(b,text="--")
    lb8.config(text="")

btn2=tk.Button(fr1,text="پاک کردن" ,font=("Tahoma" , 12),command=clean,fg="#000000",bg="#B58357")
btn2.pack(padx=10,pady=10)
btn2.propagate(False)

fr2=tk.Frame(root,bg="#1B1543",width=260 ,height=330)
fr2.pack(pady=10,padx=30,side='right')
fr2.propagate(False)

lb7=tk.Label(fr2,text="نتیجه محاسبه" , font=("Tahoma" , 14),fg="#FFFFFF" ,bg="#1B1543")
lb7.pack(padx=10,pady=10)


canvas=tk.Canvas(fr2,bg="#1B1543" , width=200 , height=200,highlightthickness=0 )
canvas.pack(pady=10)
canvas.create_oval(20,20,180,180, outline="#B58357",width=3)
canvas.create_text(100, 80,text="YOUR BMI",fill="#C2BDBD",font=("Tahoma", 10))

b=canvas.create_text(100, 115,text="--",fill="#D4AF69",font=("Tahoma", 28, "bold"))
canvas.itemconfig(b, text=round(b, 2))

lb8=tk.Label(fr2,text="" , font=("Tahoma" , 14),fg="#FFFFFF" ,bg="#1B1543")
lb8.pack(padx=10,pady=10)


root.mainloop()



