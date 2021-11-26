from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n % 2 == 0:
        print(0)
        continue
    res = -1
    while n > 0:
        if n % 2 == 0:
            if n < 10:
                res = 1
            else:
                res = 2
        n //= 10
    print(res)


