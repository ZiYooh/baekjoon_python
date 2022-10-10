import sys

a, b = map(int, sys.stdin.readline().split())
c = a-b
if c < 0:
    print(c*(-1))
else:
    print(c)