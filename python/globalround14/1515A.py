from sys import stdin

for _ in range(int(stdin.readline())):
    n, x = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    s = sum(a)
    if s < x:
        print('YES')
        print(*a)
    elif s == x:
        print('NO')
    else:
        a = sorted(a)
        cur = 0
        start = 0
        end = -1
        for idx, val in enumerate(a):
            cur += val
            if cur == x:
                if a[0] != a[-1]:
                    cur -= a[start]
                    start += 1
                else:
                    break
            if cur > x:
                end = idx + 1
                break

        if end != -1:
            print('YES')
            b = a[start:end] + a[:start] + a[end:]
            print(*b)
        else:
            print('NO')






