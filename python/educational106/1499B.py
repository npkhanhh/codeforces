from sys import stdin

for _ in range(int(stdin.readline())):
    s = stdin.readline().strip()
    has_11 = False
    res = True
    for idx in range(1, len(s)):
        if s[idx] == '1' and s[idx-1] == '1':
            has_11 = True
        if has_11 and s[idx] == '0' and s[idx-1] == '0':
            res = False
            break
    print('YES' if res else 'NO')
