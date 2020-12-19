from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    res = []
    for i in range(n // 2):
        res.append(a[i])
        res.append(a[-i - 1])
    if n % 2 == 1:
        res.append(a[n // 2])
    print(*res)
