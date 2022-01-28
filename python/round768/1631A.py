from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int,stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    for i in range(n):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
    print(max(a)*max(b))
