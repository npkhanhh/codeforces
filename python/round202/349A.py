input()
d = {25: 0, 50: 0}
a = list(map(int, input().split()))
res = 'YES'
s = 0
for i in a:
    if i != 25:
        if s < i - 25 or d[25] == 0:
            res = 'NO'
            break
        elif i == 50:
            d[25] -= 1
            s -= 25
        elif i == 100:
            if d[50] > 0:
                d[50] -= 1
                d[25] -= 1
            else:
                d[25] -= 3
            s -= 75
    if i != 100:
        s += i
        d[i] += 1
print(res)

