from tkinter import *
m=Tk()
m.title("Divison")
m.geometry("320x390")    
def division():
    try:
        n1=int(s1.get())
        n2=int(s2.get())
        res=n1/n2
        t.delete("1.0","end-1c")
        t.config(bg='green')
        t.insert(END,res)
    except ZeroDivisionError:
        t.delete("1.0","end-1c")
        t.config(bg='red')
        t.insert(END,"zero Division")
    except ValueError:
        t.delete("1.0","end-1c")
        t.config(bg='red')
        t.insert(END,"Invaild")
Label(m,text="Number 1",bg='light pink',width=10,height=2).grid(row=0)
Label(m,text="Number 2",bg='light pink',width=10,height=2).grid(row=1)
Label(m,text="Result",bg='light pink',width=10,height=2).grid(row=3)
s1=StringVar()
s2=StringVar()
e1=Entry(m,textvariable=s1,width=15).grid(row=0,column=1)
e2=Entry(m,textvariable=s2,width=15).grid(row=1,column=1)
Button(m,text="Division",command=division,width=10,bg="light green").grid(row=2,column=1)
t=Text(m,bg='light blue',width=15,height=2)
t.grid(row=3,column=1)
m.mainloop()
