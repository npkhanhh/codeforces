for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a, b = divmod(k, n - 1)
    if b == 0:
        b = -1
    print(a*n + b)

