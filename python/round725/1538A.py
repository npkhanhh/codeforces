from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    mi = 101
    mi_idx = -1
    ma = -1
    ma_idx = -1
    for idx, val in enumerate(a):
        if val > ma:
            ma = val
            ma_idx = idx
        if val < mi:
            mi = val
            mi_idx = idx
    l, r = sorted([mi_idx, ma_idx])
    print(min(r + 1, n - l, l + 1 + n - r))
