for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    a, b = list(map(int, input().split()))
    res = abs(x - y)*a
    if 2*a < b:
        res += min(x, y)*2*a
    else:
        res += min(x, y)*b
    print(res)
