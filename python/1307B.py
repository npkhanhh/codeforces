for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    a = sorted(list(map(int, input().split())), reverse=True)
    res = 0
    if x < a[0]:
        res = 1 if x in a else 2
    else:
        b, c = divmod(x, a[0])
        res = b + (1 if c > 0 else 0)
    print(res)
