for _ in range(int(input())):
    a, b, c, n = list(map(int, input().split()))
    a, b, c = sorted([a, b, c])

    if (a+b+c+n) % 3 == 0 and ((c - b) + (c-a)) <= n:
        print('YES')
    else:
        print('NO')