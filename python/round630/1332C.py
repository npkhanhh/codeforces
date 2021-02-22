from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    s = stdin.readline().strip()
    group = n // k
    res = 0
    for i in range(k//2):
        max_appear = 0
        max_appear_char = ''
        d = {}
        for j in range(group):
            idxes = [j*k+i, j*k+(k-i-1)]
            for idx in idxes:
                if s[idx] not in d:
                    d[s[idx]] = 1
                else:
                    d[s[idx]] += 1
                if d[s[idx]] > max_appear:
                    max_appear = d[s[idx]]
                    max_appear_char = s[idx]
        for char, val in d.items():
            if char != max_appear_char:
                res += val
    if k % 2 == 1:
        t = k // 2
        d = {}
        max_appear = 0
        max_appear_char = ''
        for i in range(t, n, k):
            c = s[i]
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
            if d[c] > max_appear:
                max_appear = d[c]
                max_appear_char = c
        for char, val in d.items():
            if char != max_appear_char:
                res += val
    print(res)


