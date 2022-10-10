import sys

while 1:
    try:
        b, c = map(int, sys.stdin.readline().split())
        print(b+c)
    except:
        break
