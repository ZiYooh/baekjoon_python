import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().split()))

a_min = a[0]
for i in range(n):
    if a_min > a[i]:
        a_min = a[i]
a_max = a[0]
for i in range(n):
    if a_max < a[i]:
        a_max = a[i]
print(a_min, end=" ")
print(a_max)
