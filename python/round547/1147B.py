n = int(input())
a = list(map(int, input().strip().split()*2))
res = 0
t = 0
for i in a:
    if i == 1:
        t += 1
        if t > res:
            res = t
    else:
        t = 0
print(res)
