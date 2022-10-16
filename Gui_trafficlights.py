from tkinter import *
m=Tk()
m.title("Traffic Lights")
m.geometry('520x560')
s=StringVar()
s.set('white')
def change():
    m.config(bg=s.get())
r1=Radiobutton(text='Red light',font='italic 14 bold',variable=s,value='Red',width=8,height=2,command=change).grid()
r2=Radiobutton(text='Green light',font='itlaic 14 bold',variable=s,value='Green',width=8,height=2,command=change).grid()
r3=Radiobutton(text='Yellow light',font='italic 14 bold',variable=s,value='yellow',width=8,height=2,command=change).grid()
m.mainloop()