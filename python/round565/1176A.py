from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    res = 0
    while n % 2 == 0:
        n //= 2
        res += 1
    while n % 3 == 0:
        n //= 3
        res += 2
    while n % 5 == 0:
        n //= 5
        res += 3
    if n > 1:
        res = -1
    print(res)

