import os
words=0
lines=0
chars=0
file_name=input("Enter the file name")
if (os.path.exists(file_name)):
    print("File exists ,now opening it")
    with open(file_name,'r') as f:
        for line in f:
            wordslist=line.split()
            lines+=1
            words+=len(wordslist)
            chars+=len(line)
    print("number of words :", words)
    print("Numbeer of lines :",lines)
    print("number of charcaters :",chars)
else:
    print("File does not exist..")
            
