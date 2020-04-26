a = ['B', 'W']
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    replace = n % 2 == 0 or m % 2 == 0
    for i in range(n):
        res = ''
        for j in range(m):
            res += a[(i + j) % 2]
        if i == n - 1 and replace:
            res = res.replace('W', 'B', 1)
        print(res)
