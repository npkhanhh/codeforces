for _ in range(int(input())):
    n = int(input())
    if n % 4 != 0:
        print('NO')
    else:
        print('YES')
        res = []
        s = 0
        for i in range(2, n+1, 2):
            res.append(i)
            s += i
        for i in range(2, n-1, 2):
            res.append(i-1)
            s -= i-1
        res.append(s)
        print(*res)