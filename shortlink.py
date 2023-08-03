import pyshorteners
from tkinter.ttk import *
from tkinter import *

window= Tk()
window.title("URL Shortener")
window.geometry("400x400")
def mini():
    if t2.get():
        t2.delete(0,END)
    
    if t1.get():
        link=pyshorteners.Shortener().tinyurl.short(t1.get())
        print(t2.insert(0,link))

top=Frame(window,width=1600,height=5,bg='#34495e')
top.grid(row=0,column=0)

bd=Frame(window,width=500,height=600,bg='#74556B')
bd.grid(row=1,column=0)
bd.place(x=0,y=5)

l1=Label(bd,text="Enter Link Here",font=("Helventica",20),bg='#F9FBE7')
l1.place(x=10,y=50)

t1=Entry(bd,font=("Helventica",15),width=30,bg="#DFCAC5")
t1.place(x=10,y=100)

bu=Button(bd,text="Short Link",command=mini,width=20,justify=CENTER,bg="#FFFFF3")
bu.place(x=100,y=160)

l2=Label(bd,text="Short Link",font=("Helventica",20),bg='#F9FBE7')
l2.place(x=10,y=200)

t2=Entry(bd,font=("Helventica",15),width=23,bg="#DFCAC5")
t2.place(x=10,y=250)

window.mainloop()