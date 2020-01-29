n = int(input())
s = input()
res = ''
t = 1
i = 1
while True:
    if t > len(s):
        break
    res += s[t-1]
    t += i
    i += 1
print(res)