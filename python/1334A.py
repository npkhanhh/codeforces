from sys import stdin

for _ in range(int(input())):
    res = 'YES'
    p = c = 0
    for _ in range(int(input())):
        pt, ct = list(map(int, stdin.readline().split()))
        if pt < p or ct < c:
            res = 'NO'
        elif pt - p < ct - c:
            res = 'NO'
        p, c = pt, ct
    print(res)

