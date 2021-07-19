from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    res = True
    for i in range(n-1):
        if a[i] % 2 != a[i+1] % 2:
            res = False
            break
    print('YES' if res else 'NO')
