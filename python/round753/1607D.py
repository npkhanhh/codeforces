from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    s = stdin.readline().strip()
    b = []
    r = []
    for i in range(n):
        if s[i] == 'B':
            b.append(a[i])
        else:
            r.append(a[i])
    b = sorted(b)
    r = sorted(r, reverse=True)
    max_b = 0
    for i in b:
        if i > max_b:
            max_b += 1
    min_r = n+1
    for i in r:
        if i < min_r:
            min_r -= 1
    print('YES' if max_b >= min_r - 1 else 'NO')

