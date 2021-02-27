x, y = list(map(int, input().split()))
n = int(input())
MOD = 1000000000 + 7
a = [x - y, x, y, y - x, -x, -y]
a = list(map(lambda ele: ele % MOD, a))
print(a[n % 6])
