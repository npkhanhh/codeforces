n, l, r = list(map(int, input().split()))
mi = 2 ** l - 1 + n - l
ma = 2 ** r - 1 + (2 ** (r-1)) * (n - r)
print(mi, ma)
