n, k = list(map(int, input().split()))

a = list(map(int, input().split()))
c, *a = a
if c == 0:
    print(n // k)
else:
    res = len(a)
    for i in range(1, len(a)):
        if a[i] - a[i - 1] > k:
            res += (a[i] - a[i - 1]) // k
            if (a[i] - a[i - 1]) % k == 0:
                res -= 1
    if a[0] - 1 >= k:
        res += (a[0] - 1) // k
    if n - a[-1] >= k:
        res += (n - a[-1]) // k
    print(res)
