import sys

t = int(sys.stdin.readline().strip())
a = []

for i in range(t):
    a.append(sys.stdin.readline().strip())

for j in range(t):
    print(a[j][0]+a[j][-1])
