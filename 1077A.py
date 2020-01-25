for _ in range(int(input())):
    a, b, k = list(map(int, input().split()))
    res = k//2*a - k//2*b
    if k % 2 == 1:
        res+=a
    print(res)
