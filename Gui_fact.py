from tkinter import *
m=Tk()
m.geometry("220x290")
m.title('Factorial')
def fact():
    f = int(t1.get("1.0","end-1c"))
    if f == 0 or f == 1:
        t2.delete("1.0", "end-1c")
        t2.insert(END, "1")
    else:
        result = 1
        for i in range(1,f+1):
            result = result*i
        t2.delete("1.0", "end-1c")
        t2.insert(END,result)

Label(m,text="Enter number ",bg="black",fg="white",font= 'italic 12 bold',borderwidth=2,relief= SUNKEN).pack(side = TOP,fill=X)
t1= Text(m,bg="light green",font="Courior 14 bold",width=10,height=2,borderwidth=2,relief=SUNKEN)
t1.pack(side = TOP,fill=X)
Button(m,text = "Compute",bg="blue",fg="white",width=10,height=2,command=fact,borderwidth=3,relief=SUNKEN).pack(side=TOP)
Label(m,text="Result",bg="black",fg="white",font= ("italic",12,"bold"),borderwidth=2,relief= SUNKEN).pack(side = TOP,fill=X)
t2= Text(m,bg="light green",font="Courior 14 bold",width=10,height=2,borderwidth=2,relief=SUNKEN)
t2.pack(side = TOP,fill=X)
m.mainloop()
