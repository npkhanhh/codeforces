n = int(input())
a = [0]+list(map(int, input().split()))
p = [0]*(n+1)
for i in range(1, n+1):
    group = set()
    t = i
    while t not in group:
        group.add(t)
        t = a[t]
    p[i] = t

print(*p[1:])
