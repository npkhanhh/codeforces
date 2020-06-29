for _ in range(int(input())):
    n = int(input())
    res = 0
    while n % 6 == 0:
        res += 1
        n //= 6
    while n % 3 == 0:
        res += 2
        n //= 3
    if n == 1:
        print(res)
    else:
        print(-1)

