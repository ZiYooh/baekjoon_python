import sys

while 1:
    b, c = map(int, sys.stdin.readline().split())
    if b == 0 and c == 0:
        break
    print(b+c)
