n = int(input())
res = ''
a, b = 1, 1
for i in range(1, n + 1):
    if i == b:
        res += 'O'
        a, b = b, a + b
    else:
        res += 'o'
print(res)
