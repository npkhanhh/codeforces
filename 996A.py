n = int(input())

res = 0

t, n = divmod(n, 100)
res+=t
t, n = divmod(n, 20)
res+=t
t, n = divmod(n, 10)
res+=t
t, n = divmod(n, 5)
res+=t
t, n = divmod(n, 1)
res+=t

print(res)