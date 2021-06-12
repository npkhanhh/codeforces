from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    res = 'YES'
    m = -1
    for i in a:
        if i < 0:
            res = 'NO'
            break
        if i > m:
            m = i
    print(res)
    if res == 'YES':
        print(m+1)
        print(*list(range(0, m+1)))

