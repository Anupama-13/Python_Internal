r1 = int(input("enter no of rows in matrix 1 \n"))
c1= int(input("enter no of columns in matrix 1 \n"))
r2= int(input("enter no of rows in matrix 2 \n"))
c2 = int(input("enter no of columns in matrix 2\n"))
if r1!=r2 or c1!=c2:
    print("Cannot do additon,both matrices should be equal \n")
else:
    m1 =[]
    m2 = []

    for i in range(r1):
        l = []
        for j in range(c1):
            ele=int(input("Enter ele into matrix 1"))
            l.append(ele)
        m1.append(l)
    for i in range(r2):
        l = []
        for j in range(c2):
            ele=int(input("Enter ele into matrix 2"))
            l.append(ele)
        m2.append(l)
    result = []
    for i in range(r1):
        l = []
        for j in range(c1):
            add=m1[i][j]+m2[i][j]
            l.append(add)
        result.append(l)
    print("The resultant matrix is :")
    for i in range(r1):
        for j in range(c1):
            print(result[i][j], end = " ")
        print()
