for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    d = k//2
    c = k - d
    a = n // k
    print(min(n, a*c + (a+1)*d))
