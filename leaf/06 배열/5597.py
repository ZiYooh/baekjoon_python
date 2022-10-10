import sys

array = [i for i in range(1, 31)]
for j in range (28):
    array.remove(int(sys.stdin.readline()))
print(*array, sep="\n")
