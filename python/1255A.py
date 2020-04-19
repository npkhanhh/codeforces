for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    res, c = divmod(abs(a-b), 5)
    t, d = divmod(c, 2)
    res += t + d
    print(res)