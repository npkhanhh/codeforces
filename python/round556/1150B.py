from sys import stdin

a = []

n = int(stdin.readline())
for _ in range(n):
    a.append(list(stdin.readline().rstrip()))

res = True
for i in range(n):
    for j in range(n):
        if a[i][j] == '.':
            if i >= n - 2 or j == 0 or j == n - 1:
                res = False
                break
            if a[i + 1][j - 1] == '#' or a[i + 1][j] == '#' or a[i + 1][j + 1] == '#' or a[i + 2][j] == '#':
                res = False
                break
            a[i][j] = '#'
            for k in range(j - 1, j + 2):
                a[i + 1][k] = '#'
            a[i+2][j] = '#'

    if not res:
        break

print(['NO', 'YES'][res])





