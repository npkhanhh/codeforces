from sys import stdin
from queue import Queue

for _ in range(int(stdin.readline())):
    n, m = list(map(int, stdin.readline().split()))
    a = []
    for _ in range(n):
        a.append(list(stdin.readline().strip()))
    res = [[0]*m for _ in range(n)]
    is_res = True
    start_row = 'R'
    for i in range(n):
        cur = start_row
        for j in range(m):
            if a[i][j] != '.' and cur != a[i][j]:
                is_res = False
                break
            res[i][j] = cur
            cur = 'W' if cur == 'R' else 'R'
        if not is_res:
            break
        start_row = 'W' if start_row == 'R' else 'R'
    if not is_res:
        is_res = True
        start_row = 'W'
        for i in range(n):
            cur = start_row
            for j in range(m):
                if a[i][j] != '.' and cur != a[i][j]:
                    is_res = False
                    break
                res[i][j] = cur
                cur = 'W' if cur == 'R' else 'R'
            if not is_res:
                break
            start_row = 'W' if start_row == 'R' else 'R'
    if not is_res:
        print('NO')
    else:
        print('YES')
        for i in range(n):
            print(''.join(res[i]))

