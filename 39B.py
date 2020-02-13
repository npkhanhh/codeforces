n = int(input())
a = list(map(int,input().split()))
res = []
s = 2001
t = 1
for i in range(n):
    if a[i] == t:
        res.append(s)
        t+=1
    s+=1
print(len(res))
print(*res)
