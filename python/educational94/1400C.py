from sys import stdin

for _ in range(int(stdin.readline())):
    s = stdin.readline().strip()
    n = len(s)
    x = int(stdin.readline())
    res = ['1'] * n
    for i, c in enumerate(s):
        if c == '0':
            if i + x < n:
                res[i + x] = '0'
            if i - x > -1:
                res[i - x] = '0'
    for i in range(n):
        one = False
        one = one or (i - x >= 0 and res[i - x] == '1')
        one = one or (i + x < n and res[i + x] == '1')
        cur = '1' if one else '0'
        if s[i] != cur:
            res = ['-1']
            break
    print("".join(res))
