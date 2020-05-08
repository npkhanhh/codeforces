for _ in range(int(input())):
    a, b = sorted(map(int, input().split()))
    c, d = sorted(map(int, input().split()))
    if b == d and a + c == b:
        print('YES')
    else:
        print('NO')