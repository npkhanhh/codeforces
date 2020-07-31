from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))[::-1]
    increasing = True
    res = 0
    for i in range(1, n):
        if increasing and a[i] < a[i-1]:
            increasing = False
        elif not increasing and a[i] > a[i-1]:
            res = n - i
            break
    print(res)
