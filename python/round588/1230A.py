res = 'NO'
a = list(map(int, input().split()))
t = sum(a) / 2
for i in range(2):
    if a[i] == t:
        res = 'YES'
        break
    for j in range(i+1, 3):
        if a[i] + a[j] == t:
            res = 'YES'
            break
        for k in range(j+1, 4):
            if a[i] + a[j] + a[k] == t:
                res = 'YES'
                break
print(res)
