import sys

a = int(sys.stdin.readline())
b = ""
for i in range(a):
    for j in range(i+1):
        b = b + "*"
    print(b)
    b = ""
    i = i + 1
