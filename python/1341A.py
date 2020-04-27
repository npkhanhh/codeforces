for _ in range(int(input())):
    n, a, b, c, d = list(map(int, input().split()))
    res = 'Yes'
    if (a + b) * n < c - d:
        res = 'No'
    elif (a - b) * n > c + d:
        res = 'No'
    print(res)
