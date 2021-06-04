from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    s = stdin.readline().strip()
    res = True
    ct = 0
    cm = 0
    ctr = 0
    cmr = 0
    for i in range(n):
        if s[i] == 'T':
            ct += 1
        else:
            cm += 1
            if cm > ct:
                res = False
                break
        if s[-i-1] == 'T':
            ctr += 1
        else:
            cmr += 1
            if cmr > ctr:
                res = False
                break
    if ct != cm*2:
        res = False

    print('YES' if res else 'NO')
