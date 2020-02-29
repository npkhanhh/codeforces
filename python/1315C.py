for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    check = [True] * (2 * n)
    for i in range(n):
        check[a[i]-1] = False
    res = []
    right = []
    for idx, value in enumerate(a):
        res.append(value)
        i = value - 1
        while i < 2*n and not check[i]:
            i += 1
        if i < 2*n:
            check[i] = False
            res.append(i+1)
        else:
            res = [-1]
            break
    print(*res)

