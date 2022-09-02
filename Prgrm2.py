import os
file_name=input("ENter file name : ")
if(os.path.exists(file_name)):
    print("File exsits..The contents in ascending order are..")
    with open(file_name,'r') as f:
        print(sorted(f.readlines()))
else:
    print("file does not exist")
    
