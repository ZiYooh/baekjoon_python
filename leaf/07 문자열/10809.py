import sys

a = "abcdefghijklmnopqrstuvwxyz"
b = sys.stdin.readline().strip()

for i in a:
    if i in b:
        print(b.index(i), end= ' ')
    else:
        print( -1, end =' ')
