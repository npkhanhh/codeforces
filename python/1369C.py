from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    a = sorted(map(int, stdin.readline().split()))
    w = sorted(map(int, stdin.readline().split()), reverse=True)
    res = 0
    i = 0
    j = n - 1
    i_w = 0
    j_w = k - 1
    while j_w >= i_w and w[j_w] == 1:
        res += a[j] * 2
        j -= 1
        j_w -= 1
    while i_w <= j_w:
        v = w[i_w]
        res += a[i] + a[j]
        j -= 1
        i += v-1
        i_w += 1
    print(res)

