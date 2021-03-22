from sys import stdin


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    a.append(a[0])
    cw = True
    cc = True
    f_cw = False
    f_cc = False

    for i in range(1, n+1):
        if a[i] > a[i-1]:
            if not f_cc:
                f_cc = True
            else:
                cc = False
        else:
            if not f_cw:
                f_cw = True
            else:
                cw = False
    print('YES' if cc or cw else 'NO')
