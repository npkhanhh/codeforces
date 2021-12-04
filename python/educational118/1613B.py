from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    m_idx = -1
    m = 10**6 - 1
    for idx, val in enumerate(a):
        if val < m:
            m = val
            m_idx = idx
    i = -1
    res = []
    count = 0
    while count < n // 2:
        i += 1
        if i == m_idx:
            continue
        print(a[i], m)
        count += 1
