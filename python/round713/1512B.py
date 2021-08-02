from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = []
    x1, y1 = -1, -1
    x2, y2 = -1, -1

    for i in range(n):
        s = list(stdin.readline().strip())
        a.append(s)
        for j in range(n):
            if s[j] == '*':
                if x1 == -1:
                    x1 = j
                    y1 = i
                else:
                    x2 = j
                    y2 = i
    if x1 == x2:
        if x1 == 0:
            a[y1][x1+1] = '*'
            a[y2][x2+1] = '*'
        else:
            a[y1][x1-1] = '*'
            a[y2][x2-1] = '*'
    elif y1 == y2:
        if y1 == 0:
            a[y1+1][x1] = '*'
            a[y2+1][x2] = '*'
        else:
            a[y1-1][x1] = '*'
            a[y2-1][x2] = '*'
    else:
        a[y1][x2] = '*'
        a[y2][x1] = '*'
    for i in a:
        print(''.join(i))


