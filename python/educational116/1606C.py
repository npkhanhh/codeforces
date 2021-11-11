from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    res = 0
    k+=1
    for i in range(1, n):
        t = a[i]-a[i-1]
        notes = min(k, 10**t-1)
        k -= notes
        res += notes*(10**a[i-1])
    if k > 0:
        res += k*(10**a[-1])
    print(res)



