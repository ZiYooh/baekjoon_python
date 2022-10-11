import sys

t = int(sys.stdin.readline().strip())
a = []

for i in range(t):
    a.append(list(sys.stdin.readline().split()))

for i in range(t):
    for j in range(len(a[i][1])):
        for k in range(int(a[i][0])):
            if j == len(a[i][1]) - 1 and k == int(a[i][0]) - 1:
                print(a[i][1][j])
            else:
                print(a[i][1][j], end="")
