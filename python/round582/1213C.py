from sys import stdin

for _ in range(int(stdin.readline())):
    n, m = list(map(int, stdin.readline().split()))
    t = m % 10
    a = []
    for i in range(10):
        a.append((t * i) % 10)
    s = sum(a)
    x = n // m
    x, y = divmod(x, 10)
    res = x * s + sum(a[:y+1])
    print(res)
