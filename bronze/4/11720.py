import sys

n = int(sys.stdin.readline().strip())
b = sys.stdin.readline().strip()
r = 0
for i in range(n):
    r += int(b[i])
print(r)
