from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = sorted(map(int, stdin.readline().split()))
    min_diff = a[-1] - a[0]
    min_idx = 0
    for i in range(1, n):
        if a[i] - a[i-1] < min_diff:
            min_diff = a[i] - a[i-1]
            min_idx = i
    res = a[min_idx:] + a[:min_idx]
    print(*res)
