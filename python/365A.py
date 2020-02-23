n, k = list(map(int,input().split()))

t2 = range(0, k + 1)
res = 0
for _ in range(n):
    s = input()
    accept = True
    for i in t2:
        if str(i) not in s:
            accept = False
            break
    if accept:
        res+=1
print(res)