for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    print('YES' if a % b == 0 else 'NO')