from sys import stdin

for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, stdin.readline().split()))
    t = a[1] - a[0]
    for i in range(1, n):
        if a[i] - a[i-1] < t:
            t = a[i] - a[i-1]
    print(t)
