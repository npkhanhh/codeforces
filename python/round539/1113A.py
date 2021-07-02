n, v = list(map(int, input().split()))
if v >= n-1:
    print(n-1)
else:
    t = n-v
    res = v + t*(t+1)//2 - 1
    print(res)
