for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    res = 'NO'
    if n == 1 or m == 1 or (n == 2 and m == 2):
        res = 'YES'
    print(res)