import sys
import os
file_1=sys.argv[1]
file_2=sys.argv[2]
try:
    with open(file_1,'r') as f1,open(file_2,'w')as f2:
        k=f1.read()
        f2.write(k)
        print("file copied successfully")
except :
    print("File not found error")
