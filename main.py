n = int(input())
s = input()
r = 0
n = int(n / 2)
res = ''
for i in range(n):
    if s[i * 2] == s[i * 2 + 1]:
        res += 'ab'
        r += 1
    else:
        res += s[i * 2:i * 2 + 2]
print(r)
print(res)
