import sys
file_name=sys.argv[1]
n=int(sys.argv[2])
with open(file_name,'r')as f:
    f.seek(n)
    print(f.read())
