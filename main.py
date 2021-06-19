from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("365x503")
root.minsize(370, 503)
root.maxsize(370, 503)
root.title("Tkinter's_Calculator")
root.wm_iconbitmap(None)


def click(event):

    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
    
def DialogBox(event):
   print("work in process")

def singleword(event):
    pass



scvalue = StringVar()
scvalue.set("0")
screen = Entry(root, textvar=scvalue, font="Poppins 40 bold",bg = "gray90")
screen.pack(fill=X, padx=11, pady=11)


f = Frame(root, bg="grey", relief=SUNKEN)
f.pack(fill=X)

b = Button(f, text="%", font="200", padx=27, pady=20, bg="grey",fg="White")
b.pack(side=LEFT, padx=3, pady=3)
b.bind("<Button-1>", click) 
b.bind("<Double-Button-1>", singleword)

b = Button(f, text="/", font="200", padx=32, pady=20, bg="grey",fg="White")
b.pack(side=LEFT, padx=3, pady=3)
b.bind("<Button-1>", click) 
b.bind("<Double-Button-1>", singleword)

b = Button(f, text="C", font="200", padx=80, pady=20, bg="dodger blue")
b.pack(side=LEFT, padx=3, pady=3)
b.bind("<Button-1>", click) 
b.bind("<Double-Button-1>", singleword)


f = Frame(root, bg="grey", relief=SUNKEN)
f.pack(fill=X)

b = Button(f, text="7", font="200", padx=30, pady=20, bg="white smoke")
b.pack(side=LEFT, padx=3, pady=3)
b.bind("<Button-1>", click) 
b.bind("<Double-Button-1>", singleword)

b = Button(f, text="8", font="200", padx=30, pady=20, bg="white smoke")
b.pack(side=LEFT, padx=3, pady=3)
b.bind("<Button-1>", click) 
b.bind("<Double-Button-1>", singleword)

b = Button(f, text="9", font="200", padx=30, pady=20, bg="white smoke")
b.pack(side=LEFT, padx=3, pady=3)
b.bind("<Button-1>", click) 
b.bind("<Double-Button-1>", singleword)

b = Button(f, text="*", font="200", padx=35, pady=20, bg="grey",fg="White")
b.pack(side=LEFT, padx=3, pady=3)
b.bind("<Button-1>", click) 
b.bind("<Double-Button-1>", singleword)


f = Frame(root, bg="grey", relief=SUNKEN)
f.pack(fill=X)

b = Button(f, text="4", font="200", padx=30, pady=20, bg="white smoke")
b.pack(side=LEFT, padx=3, pady=3)
b.bind("<Button-1>", click) 
b.bind("<Double-Button-1>", singleword)

b = Button(f, text="5", font="200", padx=30, pady=20, bg="white smoke")
b.pack(side=LEFT, padx=3, pady=3)
b.bind("<Button-1>", click)
b.bind("<Double-Button-1>", singleword)

b = Button(f, text="6", font="200", padx=30, pady=20, bg="white smoke")
b.pack(side=LEFT, padx=3, pady=3)
b.bind("<Button-1>", click) 
b.bind("<Double-Button-1>", singleword)

b = Button(f, text="-", font="200", padx=35, pady=20, bg="grey",fg="White")
b.pack(side=LEFT, padx=3, pady=3)
b.bind("<Button-1>", click) 
b.bind("<Double-Button-1>", singleword)


f = Frame(root, bg="grey", relief=SUNKEN)
f.pack(fill=X)

b = Button(f, text="1", font="200", padx=30, pady=20, bg="white smoke")
b.pack(side=LEFT, padx=3, pady=3)
b.bind("<Button-1>", click) 
b.bind("<Double-Button-1>", singleword)

b = Button(f, text="2", font="200", padx=30, pady=20, bg="white smoke")
b.pack(side=LEFT, padx=3, pady=3)
b.bind("<Button-1>", click) 
b.bind("<Double-Button-1>", singleword)

b = Button(f, text="3", font="200", padx=29.5, pady=20, bg="white smoke")
b.pack(side=LEFT, padx=3, pady=3)
b.bind("<Button-1>", click) 
b.bind("<Double-Button-1>", singleword)

b = Button(f, text="+", font="200", padx=35, pady=20, bg="grey",fg="White")
b.pack(side=LEFT, padx=3, pady=3)
b.bind("<Button-1>", click) 
b.bind("<Double-Button-1>", singleword)


f = Frame(root, bg="grey", relief=SUNKEN)
f.pack(fill=X)

b = Button(f, text="0", font="200", padx=76, pady=20, bg="white smoke")
b.pack(side=LEFT, padx=3, pady=3)
b.bind("<Button-1>", click) 
b.bind("<Double-Button-1>", singleword)
b.bind("<Double-Button-1>", DialogBox)

b = Button(f, text=".", font="200", padx=32, pady=20, bg="grey",fg="White")
b.pack(side=LEFT, padx=3, pady=3)
b.bind("<Button-1>", click) 
b.bind("<Double-Button-1>", singleword)

b = Button(f, text="=", font="200", padx=36, pady=20, bg="orange2")
b.pack(side=LEFT, padx=3, pady=3)
b.bind("<Button-1>", click) 
b.bind("<Double-Button-1>", singleword)

#Dialog BOx
tmsg._show("Tips & Tricks","Double Click on 0 - for more themes")
root.mainloop()
