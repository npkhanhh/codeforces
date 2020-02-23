for _ in range(int(input())):
    n = int(input())
    res = n
    while True:
        n, b = divmod(n, 10)
        if n > 0:
            res += n
            n += b
        else:
            break
    print(res)