from sys import stdin

for _ in range(int(stdin.readline())):
    r, c = list(map(int, stdin.readline().split()))
    res = True
    for i in range(r):
        a = list(map(int, stdin.readline().split()))
        for idx, val in enumerate(a):
            if i == 0 or i == r - 1:
                if val > 3:
                    res = False
                if idx == 0 or idx == c - 1:
                    if val > 2:
                        res = False
            if (idx == 0 or idx == c - 1) and val > 3:
                res = False
            if val > 4:
                res = False
    if not res:
        print('NO')
    else:
        print('YES')
        for i in range(r):
            if i == 0 or i == r - 1:
                a = [2] + [3] * (c - 2) + [2]
            else:
                a = [3] + [4] * (c - 2) + [3]
            print(*a)
