for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    res = n - 1
    lowest = a[-1]
    for i in range(n-2, -1, -1):
        if a[i] <= lowest:
            res -= 1
            lowest = a[i]
    print(res)
