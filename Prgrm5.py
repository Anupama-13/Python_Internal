class Rectangle:
    def __init__(self,l,b):
        self.l=l;
        self.b=b;
    def area(self):
        print("The area is",self.l*self.b)
    def perimeter(self):
        print("The perimeter is",2*(self.l+self.b))
    def isSquare(self):
        if self.l==self.b:
            return True
        else:
            return False
    def disp_len(self):
        return self.l
    def disp_breadth(self):
        return self.b
l=int(input("enter length.."))
b=int(input("enter breadth.."))
r=Rectangle(l,b)
r.area()
r.perimeter()
print("is the rectaangle square..",r.isSquare())
print("The length is.",r.disp_len())
print("The breadth is..",r.disp_breadth())
