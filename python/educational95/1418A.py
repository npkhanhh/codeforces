from sys import stdin

for _ in range(int(stdin.readline())):
    x, y, k = list(map(int, stdin.readline().split()))
    res = k
    a, b = divmod(k*(y + 1) - 1, (x-1))
    res += a
    if b > 0:
        res += 1
    print(res)

