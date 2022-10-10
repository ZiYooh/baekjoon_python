import sys


def alpha(a, b):
    return (a+b)*(a-b)


a, b = map(int, sys.stdin.readline().split())
print(alpha(a, b))
