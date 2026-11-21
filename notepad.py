import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


root=tk.Tk()
root.geometry("700x500")
root.title("notepad")


def openfile():
    o=filedialog.askopenfilename(title="یک فایل را انتخاب کن" , filetypes=[("txtfile", "*.txt") , ( "all files", "*.*")])
    if o:
        with open(o , "r" , encoding="Utf-8") as f:
            openfiles=f.read()
            txt.delete("1.0" , tk.END)
            txt.insert("1.0" , openfiles)

def savefile():
    s=filedialog.asksaveasfilename(title="یک فایل را انتخاب کن" , filetypes=[("txtfile", "*.txt") , ( "all files", "*.*")],defaultextension=".txt")
    if s:
        with open(s,"w" , encoding="Utf-8") as f:
           i=txt.get("1.0" , tk.END)

           a= f.write(i)
           if a:
               messagebox.showinfo("ذخیره شد")           

menubar=tk.Menu(root)

menu2=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=menu2)
menu3=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=menu3)
menu4=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Format",menu=menu4)
menu5=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="View",menu=menu5)
menu6=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=menu6)


menu2.add_command(label="New",accelerator="Ctrl+N")
menu2.add_command(label="New Window",accelerator="Ctrl+Shift+N")
menu2.add_command(label="Open...",accelerator="Ctrl+O",command=openfile)
menu2.add_command(label="Save",accelerator="Ctrl+S",command=savefile)
menu2.add_command(label="Save As...",accelerator="Ctrl+Shift+S")
menu2.add_separator()
menu2.add_command(label="Page Setup...")
menu2.add_command(label="Print",accelerator="Ctrl+P")
menu2.add_separator()
menu2.add_command(label="Exit")





menu3.add_command(label="Undo",accelerator="Ctrl+Z")
menu3.add_separator()
menu3.add_command(label="Cut",accelerator="Ctrl+X")
menu3.add_command(label="Copy",accelerator="Ctrl+C")
menu3.add_command(label="Paste",accelerator="Ctrl+V")
menu3.add_command(label="Delete",accelerator="Del")
menu3.add_separator()
menu3.add_command(label="Search with Bing" , accelerator="Ctrl+E")
menu3.add_command(label="Find...",accelerator="Ctrl+F")
menu3.add_command(label="Find Next" , accelerator="F3")
menu3.add_command(label="Find Previous",accelerator="Shift+F3")
menu3.add_command(label="Replace",accelerator="Ctrl+H")
menu3.add_command(label="Go To",accelerator="Ctrl+G")
menu3.add_separator()
menu3.add_command(label="Selecte All",accelerator="Ctrl+A")
menu3.add_command(label="Time/Date",accelerator="F5")



menu4.add_command(label="Word Wrap")
menu4.add_command(label="Font...")




menu5.add_command(label="Zoom")
menu5.add_command(label="Status Bar")






menu6.add_command(label="View Help")
menu6.add_command(label="Send Feedback")
menu6.add_separator()
menu6.add_command(label="About Notepad")

scrol=tk.Scrollbar(root)
scrol.pack(fill="y" , side="right")
txt=tk.Text(root , font="Tahoma",yscrollcommand=scrol.set)
txt.pack(fill="both" , expand=True)


root.config(menu=menubar)
root.mainloop()


