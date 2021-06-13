from sys import stdin


for _ in range(int(stdin.readline())):
    n, m = list(map(int, stdin.readline().split()))
    s = list(stdin.readline().strip())
    for i in range(m):
        changed = False
        new_s = ['0']*n
        for idx in range(n):
            if s[idx] == '1':
                new_s[idx] = '1'
            if 0 < idx < n - 1 and s[idx - 1] == '1' and s[idx + 1] == '1':
                continue
            if s[idx] == '0' and (idx> 0 and s[idx-1] == '1' or idx<n-1 and s[idx+1] == '1'):
                changed = True
                new_s[idx] = '1'
        s = new_s
        if not changed:
            break
    print(''.join(s))


