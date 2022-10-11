import sys

a = []
for i in range(9):
    a.append(int(sys.stdin.readline().strip()))
a_max = a[0]
idx = 1
for i in range(9):
    if a_max < a[i]:
        a_max = a[i]
        idx = i + 1
print(a_max)
print(idx)
