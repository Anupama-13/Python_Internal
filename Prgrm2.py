import os
file_name=input("ENter file name : ")
if(os.path.exists(file_name)):
    print("File exsits..The contents in ascending order are..")
    l=[]
    with open(file_name,'r') as f:
        for line in f:
            l.append(line)
        l.sort()
        print(l)
else:
    print("file does not exist")
    
