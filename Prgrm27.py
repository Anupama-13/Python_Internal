file_name=input("Enter file name")
with open(file_name,'r')as f:
    l=f.readline()
    freq={}
    space=""
    while l!=space:
        for word in l.strip("\n").split(" "):
            if word in freq:
                freq[word]=freq.get(word)+1
            else:
                freq[word]=1
        l=f.readline()
for i in freq:
    print(i," --> ",freq[i])
