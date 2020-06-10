from sys import stdin

for _ in range(int(stdin.readline())):
    n, m = list(map(int, stdin.readline().split()))
    row = [True]*n
    column = [True]*m
    for i in range(n):
        a = list(map(int, stdin.readline().split()))
        for index, value in enumerate(a):
            if value == 1:
                column[index] = False
                row[i] = False
    r = row.count(True)
    c = column.count(True)
    t = min(r, c)
    if t % 2 == 0:
        print('Vivek')
    else:
        print('Ashish')
