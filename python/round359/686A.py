from sys import stdin

n, x = list(map(int, stdin.readline().split()))
res = 0
for _ in range(n):
    a, d = stdin.readline().split()
    d = int(d)
    if a == '+':
        x += d
    else:
        if x >= d:
            x -= d
        else:
            res += 1

print(x, res)

