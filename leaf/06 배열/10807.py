import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())
count = 0

for i in range(n):
    if array[i] == v:
        count = count + 1

print(count)
