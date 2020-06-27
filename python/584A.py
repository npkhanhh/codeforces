
n, t = list(map(int, input().split()))
if t == 10 and n == 1:
    print(-1)
else:
    if t == 10:
        t = 1
    print(t*(10**(n-1)))
