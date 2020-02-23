n = int(input())
s = input()
x_c = 0
res = 0
for i in s:
    if i == 'x':
        x_c += 1
        if x_c >= 3:
            res += 1
    else:
        x_c = 0
print(res)