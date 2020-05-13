for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    result = True
    a = []
    if k > n or (n > 2 and n - k == 1) or (n % 2 == 1 and k % 2 == 0) or \
            (n / k < 2 and n % 2 == 0 and n % 2 != k % 2 and n != k):
        result = False
    else:
        if n % 2 != k % 2:
            a = [2] * (k - 1)
            a.append(n - 2 * (k - 1))
        else:
            a = [1] * (k - 1)
            a.append(n - k + 1)
    if result:
        print('YES')
        print(*a)
    else:
        print('NO')
