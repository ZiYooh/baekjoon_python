import sys

a = ""
for i in sys.stdin.readline().strip():
    if i.isupper():
        a += i.lower()
    elif i.islower():
        a += i.upper()
print(a)
