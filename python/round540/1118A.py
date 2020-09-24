from sys import stdin

for _ in range(int(stdin.readline())):
    q, a, b = list(map(int, stdin.readline().split()))
    c, d = divmod(q, 2)
    print(min(q * a, b * c + d * a))
