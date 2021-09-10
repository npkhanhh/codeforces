from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    s = stdin.readline().strip()
    a = []
    for i in range(n):
        if s[i] == '2':
            a.append(i)
    if len(a) == 1 or len(a) == 2:
        print('NO')
    else:
        print('YES')
        res = [['=']*n for _ in range(n)]
        for i in range(n):
            res[i][i] = 'X'
        if len(a) > 0:
            a.append(a[0])
            for i in range(1, len(a)):
                res[a[i-1]][a[i]] = '+'
                res[a[i]][a[i-1]] = '-'
        for i in range(n):
            print(''.join(res[i]))

