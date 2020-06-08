n = int(input())
a = list(map(int, input().split()))
res = [[],[],[]]
for idx, val in enumerate(a):
    res[val-1].append(idx+1)
t = n
for i in res:
    t = min(len(i), t)
print(t)
for i in range(t):
    print(*[res[0][i], res[1][i], res[2][i]])
