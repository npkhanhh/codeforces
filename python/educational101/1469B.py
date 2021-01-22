from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    r = list(map(int, stdin.readline().split()))
    m = int(stdin.readline())
    b = list(map(int, stdin.readline().split()))
    mr, mb = r[0], b[0]
    cr, cb = r[0], b[0]
    for i in r[1:]:
        cr += i
        if cr > mr:
            mr = cr
    for i in b[1:]:
        cb += i
        if cb > mb:
            mb = cb
    print(max(0, mr+mb, mr, mb))
