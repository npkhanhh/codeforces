from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    total = sum(a)
    if k == 1:
        if total % 2 == 1:
            print('YES')
            print(n)
        else:
            print('NO')
    else:
        cur = 0
        cur_total = 0
        res = []
        for idx, val in enumerate(a):
            cur += val
            cur_total += val
            if cur % 2 == 1:
                res.append(idx + 1)
                cur = 0
                k -= 1
                if k == 1:
                    t = total - cur_total
                    if t % 2 == 1:
                        res.append(n)
                    else:
                        res = []
                    k = 0
                    break
        if k > 0 or len(res) == 0:
            print('NO')
        else:
            print('YES')
            print(*res)
