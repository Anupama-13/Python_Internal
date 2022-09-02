import os
file_name=input("Enter file name : ")
string=input("Enter any string : ")
if(os.path.exists(file_name)):
    print("File exists, now opening it..")
    with open(file_name,'r') as f:
        for line in f.readlines():
            if string in line:
                print(line)
else:
    print("File does not exist")
