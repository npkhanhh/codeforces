n, k = list(map(int, input().split()))
res = 0
time = 0
t = 240 - k
for i in range(1, n+1):
    if time + (5 * i) <= t:
        res += 1
        time += 5*i
    else:
        break
print(res)
