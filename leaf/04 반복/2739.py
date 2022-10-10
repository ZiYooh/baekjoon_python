import sys

a = int(sys.stdin.readline())
for i in range(9):
    b = a * (i+1)
    print(f"{a} * {i+1} = {b}")
