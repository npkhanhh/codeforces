from sys import stdin

for _ in range(int(stdin.readline())):
    x, y = sorted(map(int, stdin.readline().split()))
    res = x*2

    if y > x:
        y -= x
        res += 1
        y -= 1
        res += y*2
    print(res)

