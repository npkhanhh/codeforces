from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    t = a[0]
    for i in range(1, n):
        t &= a[i]
    print(t)
