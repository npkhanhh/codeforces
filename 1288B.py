for _ in range(int(input())):
    A, B = list(map(int, input().split()))
    res = 0
    seed = 9
    while seed <= B:
        res += A
        seed = seed*10 + 9
    print(res)
