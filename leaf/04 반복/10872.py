import sys

a = int(sys.stdin.readline())
r = 1
for i in range(a):
    r = r * (i+1)

print(r)
