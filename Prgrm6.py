class complex:
    def __init__(self,re,im):
        self.re=re
        self.im=im
    def __add__(self,other):
        return complex(self.re+other.re,self.im+other.im)
    def __sub__(self,other):
        return complex(self.re-other.re,self.im-other.im)
    def __mul__(self,other):
        real=(self.re*other.re)-(self.im*other.im)
        imag=(self.re*other.im)+(self.im*other.re)
        return complex(real,imag)
    def display(self):
        print(self.re,'+ (',self.im,')i')
r1=float(input("enter real value of complex number1"))
i1=float(input("enter imaginary value of complex number1"))
r2=float(input("enter real value of complex number2"))
i2=float(input("enter imaginary value of complex number2"))
c1=complex(r1,i1)
c2=complex(r2,i2)
c3=c1+c2
print("Addition of complex numbers is(real,imag):")
c3.display()
c3=c1-c2
print("Subtraction of complex numbers is:")
c3.display()
c3=c1*c2
print("Multiplication of complex numbers is:")
c3.display()


