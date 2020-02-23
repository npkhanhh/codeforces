for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for i in range(n):
        if a[i] == 0:
            res += 1
            a[i] += 1
    if sum(a) == 0:
        res += 1
    print(res)
