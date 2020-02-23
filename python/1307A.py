for _ in range(int(input())):
    n, d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    res = a[0]
    for i in range(1, n):
        if a[i] * i <= d:
            d -= a[i] * i
            res += a[i]
        else:
            res += (d // i)
            break
    print(res)



