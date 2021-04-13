k = int(input())

a = []
for i in range(19, 11**7, 9):
    t = i
    temp = t
    s = 0
    while temp > 0:
        s += temp %10
        temp //= 10
    if s == 10:
        a.append(i)

print(len(a))
