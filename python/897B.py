
k, p = list(map(int, input().split()))
res = 0
for i in range(1, k+1):
    res = (res + int(str(i) + str(i)[::-1])) % p


print(res)



