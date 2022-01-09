n, x = list(map(int, input().split()))
a = abs(sum(map(int, input().split())))
b, c = divmod(a, x)
print(b + (c != 0))
