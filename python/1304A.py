for _ in range(int(input())):
    x, y, a, b = list(map(int, input().split()))
    res, t = divmod((y-x), (a+b))
    print(res if t == 0 else -1)