n = input()
a = [0]*9

t = len(n)-1
for i in range(t, -1, -1):
    digit = int(n[i])
    p = t - i
    for j in range(digit):
        a[j] += pow(10,p)

for i in range(9):
    if a[i] == 0:
        a = a[:i]
        break
print(len(a))
print(*a)

