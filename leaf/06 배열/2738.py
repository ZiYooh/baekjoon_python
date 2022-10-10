import sys

a, b = map(int, sys.stdin.readline().split())
array_1 = []
array_2 = []

for i in range(a):
    array_1.append(list(map(int, sys.stdin.readline().split())))

for i in range(a):
    array_2.append(list(map(int, sys.stdin.readline().split())))

for i in range(a):
    for j in range(b):
        if j == b-1:
            print(array_1[i][j]+array_2[i][j])
        else:
            print(array_1[i][j] + array_2[i][j], end=" ")
