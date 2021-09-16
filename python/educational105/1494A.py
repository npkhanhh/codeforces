from sys import stdin
from collections import Counter

for _ in range(int(stdin.readline())):
    s = stdin.readline().strip()
    if s[0] == s[-1]:
        print('NO')
        continue
    c = Counter(s)
    t = sorted(c.values())
    if len(t) == 2 and t[0] != t[1] or len(t) == 3 and t[2] != t[0] + t[1]:
        print('NO')
        continue

    d = {'A': '', 'B': '', 'C': ''}
    d[s[0]] = '('
    d[s[-1]] = ')'
    for key in d.keys():
        if d[key] == '':
            d[key] = ')' if c[s[0]] > c[s[-1]] else '('
            break
    cur = 0
    res = 'YES'
    for i in s:
        if d[i] == '(':
            cur += 1
        else:
            if cur == 0:
                res = 'NO'
                break
            else:
                cur -= 1
    if cur != 0:
        res = 'NO'
    print(res)
