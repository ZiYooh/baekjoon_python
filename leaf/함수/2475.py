import sys


def check_num(a, b, c, d, e):
    ret = (a*a + b*b + c*c + d*d + e*e) % 10
    return ret


a, b, c, d, e = map(int, sys.stdin.readline().split())
print(check_num(a, b, c, d, e))
