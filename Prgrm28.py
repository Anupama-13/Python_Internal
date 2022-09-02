def palindrome(s):
    return s==s[::-1]
s=input("enter any string")
if (palindrome(s)):
    print("The string is palindrome")
else:
    print("Not palindrome")
