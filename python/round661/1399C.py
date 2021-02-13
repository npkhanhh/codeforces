from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    count = [0] * (n + 1)
    for i in a:
        count[i] += 1
    res = 0
    for i in range(2, 2 * n + 1):
        t = 0
        for j in range(1, (i + 1) // 2):
            if i - j <= n:
                t += min(count[j], count[i - j])
        if i % 2 == 0:
            t += count[i // 2] // 2
        res = max(res, t)
    print(res)
