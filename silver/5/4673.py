import sys


def make_number(input):
    a = int(input / 1000)
    b = int((input / 100) % 10)
    c = int((input / 10) % 10)
    d = int(input % 10)

    return input + a + b + c + d

temp = []
for i in range(10000):
    temp.append(make_number(i+1))

for j in range(10000):
    if j+1 not in temp:
        print(j+1)
