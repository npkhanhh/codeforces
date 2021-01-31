from sys import stdin

for _ in range(int(stdin.readline())):
    w, h, n = list(map(int, stdin.readline().split()))
    t = 1
    while w % 2 == 0:
        w //= 2
        t *= 2
    while h % 2 == 0:
        h //= 2
        t *= 2
    if t >= n:
        print("YES")
    else:
        print("NO")
