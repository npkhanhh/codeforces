from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    b= [0, 0]
    s = 0
    for t in a:
        b[t-1] += 1
        s += t
    if s % 2 == 0:
        if (b[1] % 2 == 1 and b[0] > 1 and b[0] % 2 == 0) or b[1] % 2 == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
