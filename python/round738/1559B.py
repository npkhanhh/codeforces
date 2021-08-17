from sys import stdin

s = ['B', 'R']
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(stdin.readline().strip())
    for i in range(1, n):
        if a[i] == '?':
            if a[i-1] == 'B':
                a[i] = 'R'
            elif a[i-1] == 'R':
                a[i] = 'B'
    if a[n-1] == '?':
        a[n-1] = 'B'
    for i in range(n-2, -1, -1):
        if a[i] == '?':
            if a[i+1] == 'B':
                a[i] = 'R'
            elif a[i+1] == 'R':
                a[i] = 'B'
    print(''.join(a))








