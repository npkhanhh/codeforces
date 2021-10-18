from sys import stdin

for _ in range(int(stdin.readline())):
    a, b, c = list(map(int, stdin.readline().split()))
    res = 0
    if c // 2 <= b:
        res += 3 * (c//2)
        b -= c // 2
    else:
        res += 3*b
        b = 0
    if b // 2 <= a:
        res += 3 * (b//2)
    else:
        res += 3*a
    print(res)
