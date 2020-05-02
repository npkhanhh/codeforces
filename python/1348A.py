for _ in range(int(input())):
    n = int(input())
    a, b = 0, 0
    i = 1
    while i <= (n - 2) // 2:
        a += 2**i
        i += 1

    while i <= (n - 1):
        b += 2**i
        i += 1
    a += 2**i
    print(abs(a-b))
