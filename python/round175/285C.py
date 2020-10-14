n = int(input())
a = sorted(map(int, input().split()))
res = 0
for i in range(n):
    res += abs(i+1 - a[i])
print(res)
