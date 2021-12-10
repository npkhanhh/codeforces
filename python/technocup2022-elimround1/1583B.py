from sys import stdin

for _ in range(int(stdin.readline())):
    n, m = list(map(int, stdin.readline().split()))
    avail = [True]*n
    for _ in range(m):
        a, b, c = list(map(int, stdin.readline().split()))
        avail[b-1] = False
    t = avail.index(True) + 1
    for i in range(n):
        if i + 1 == t:
            continue
        print(i+1, t)

