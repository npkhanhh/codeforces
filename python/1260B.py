for _ in range(int(input())):
    a, b = sorted(list(map(int, input().split())))
    if b > 2*a:
        print('NO')
    else:
        print('YES' if (a + b) % 3 == 0 else 'NO')