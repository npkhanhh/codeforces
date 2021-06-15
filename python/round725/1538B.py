from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = sorted(map(int, stdin.readline().split()), reverse=True)
    s = sum(a)
    if s % n != 0:
        print(-1)
    else:
        t = s // n
        res = 0
        for i in a:
            if i <= t:
                break
            res += 1
        print(res)
