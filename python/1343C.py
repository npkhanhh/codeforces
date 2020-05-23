from sys import stdin

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, stdin.readline().split()))
    sign = 1 if a[0] > 0 else -1
    biggest = a[0]
    res = 0
    for idx, value in enumerate(a):
        if value*sign < 0:
            res += biggest
            biggest = value
            sign = 1 if value > 0 else -1
        elif value > biggest:
            biggest = value
    res += biggest
    print(res)



