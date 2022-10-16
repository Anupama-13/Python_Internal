from tkinter import*
m=Tk()
m.geometry('320x380')
m.title('Calculator')
m.resizable('false','false')
f1=Frame(m,bg='white')
f1.pack(side=TOP,fill=X)
f2=Frame(m,bg='grey')
f2.pack(anchor=NW,fill=X)
def zero():
    t.insert(END,'0')
def one():
    t.insert(END,'1')
def two():
    t.insert(END,'2')
def three():
    t.insert(END,'3')
def four():
    t.insert(END,'4')
def five():
    t.insert(END,'5')
def six():
    t.insert(END,'6')
def seven():
    t.insert(END,'7')
def eight():
    t.insert(END,'8')
def nine():
    t.insert(END,'9')
def clear():
    t.delete('1.0','end-1c')
def delete():
    t.delete('end-2c','end-1c')
def add():
    t.insert(END,'+')
def sub():
    t.insert(END,'-')
def mul():
    t.insert(END,'*')
def div():
    t.insert(END,'/')
def ans():
    v=t.get('1.0','end-1c')
    try:
        res=eval(v)
        t.insert(END,'=')
        t.insert(END,res)
    except:
        res='Synatx error'
        t.delete("1.0",'end-1c')
        t.insert(END,res)
t=Text(f1,bg='white',font='italic 12 bold',width=10,height=3,borderwidth=3)
t.pack(fill=X)
Button(f2,text='1',font='italic 10 bold',bg='black',fg='white',width=6,height=4,command=one,borderwidth=3).grid(row=0,column=0)
Button(f2,text='2',font='italic 10 bold',bg='black',fg='white',width=6,height=4,command=two,borderwidth=3).grid(row=0,column=1)
Button(f2,text='3',font='italic 10 bold',bg='black',fg='white',width=6,height=4,command=three,borderwidth=3).grid(row=0,column=2)
Button(f2,text='4',font='italic 10 bold',bg='black',fg='white',width=6,height=4,command=four,borderwidth=3).grid(row=1,column=0)
Button(f2,text='5',font='italic 10 bold',bg='black',fg='white',width=6,height=4,command=five,borderwidth=3).grid(row=1,column=1)
Button(f2,text='6',font='italic 10 bold',bg='black',fg='white',width=6,height=4,command=six,borderwidth=3).grid(row=1,column=2)
Button(f2,text='7',font='italic 10 bold',bg='black',fg='white',width=6,height=4,command=seven,borderwidth=3).grid(row=2,column=0)
Button(f2,text='8',font='italic 10 bold',bg='black',fg='white',width=6,height=4,command=eight,borderwidth=3).grid(row=2,column=1)
Button(f2,text='9',font='italic 10 bold',bg='black',fg='white',width=6,height=4,command=nine,borderwidth=3).grid(row=2,column=2)
Button(f2,text='0',font='italic 10 bold',bg='black',fg='white',width=6,height=4,command=zero,borderwidth=3).grid(row=3,column=0)
Button(f2,text='+',font='italic 10 bold',bg='black',fg='white',width=6,height=4,command=add,borderwidth=3).grid(row=0,column=3)
Button(f2,text='-',font='italic 10 bold',bg='black',fg='white',width=6,height=4,command=sub,borderwidth=3).grid(row=1,column=3)
Button(f2,text='*',font='italic 10 bold',bg='black',fg='white',width=6,height=4,command=mul,borderwidth=3).grid(row=2,column=3)
Button(f2,text='/',font='italic 10 bold',bg='black',fg='white',width=6,height=4,command=div,borderwidth=3).grid(row=3,column=3)
Button(f2,text='cl',font='italic 10 bold',bg='black',fg='white',width=6,height=4,command=clear,borderwidth=3).grid(row=3,column=2)
Button(f2,text='del',font='italic 10 bold',bg='black',fg='white',width=6,height=4,command=delete,borderwidth=3).grid(row=3,column=1)
Button(f2,text='=',font='italic 10 bold',bg='orange',fg='white',width=8,height=4,command=ans,borderwidth=3).grid(row=1,column=4)
m.mainloop()