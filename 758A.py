input()
a = list(map(int, input().split()))

res = 0
m = max(a)
for i in a:
    res+=m - i
print(res)