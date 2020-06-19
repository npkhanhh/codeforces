from sys import stdin

for _ in range(int(stdin.readline())):
    a, b, n = list(map(int, stdin.readline().split()))
    if b < a:
        b, a = a, b
    count = 0
    while a <= n and b <= n:
        a += b
        a, b = b, a
        count += 1
    print(count)

