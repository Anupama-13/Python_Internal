class complex:
    def __init__(self):
        self.re=0
        self.im=0
    def readCom(self,re,im):
        self.re=re
        self.im=im
    def __add__(self,other):
        t=complex()
        t.re=self.re+other.re
        t.im=self.im+other.im
        return t
    def __sub__(self,other):
        t=complex()
        t.re=self.re-other.re
        t.im=self.im-other.im
        return t
    def __mul__(self,other):
        t=complex()
        t.re=(self.re*other.re)-(self.im*other.im)
        t.im=(self.re*other.im)+(self.im*other.re)
        return t
    def disp(self):
        print("(" ,self.re,"+",self.im,"i)")

c1=complex()
r1=float(input("enter real value of complex number1"))
i1=float(input("enter imaginary value of complex number1"))
r2=float(input("enter real value of complex number2"))
i2=float(input("enter imaginary value of complex number2"))
c2=complex()
c1.readCom(r1,i1)
c2.readCom(r2,i2)
c3=complex()
c3=c1+c2
print("Addition of complex numbers is:")
c3.disp()
c3=c1-c2
print("Subtraction of complex numbers is:")
c3.disp()
c3=c1*c2
print("Multiplication of complex numbers is:")
c3.disp()

