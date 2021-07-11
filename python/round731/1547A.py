from sys import stdin

for _ in range(int(stdin.readline())):
    stdin.readline()
    xa, ya = list(map(int, stdin.readline().split()))
    xb, yb = list(map(int, stdin.readline().split()))
    xf, yf = list(map(int, stdin.readline().split()))
    res = abs(xa-xb) + abs(ya-yb)
    if (xa == xb == xf and (ya < yf < yb or yb < yf < ya)) or (ya == yb == yf and (xa < xf < xb or xb < xf < xa)):
        res += 2
    print(res)

