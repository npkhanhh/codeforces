n = int(input())
s = "ROYGBIV"
a, b = divmod(n, len(s))
res = s * a
start = 3 if b <= 4 else 0
res += s[start:start+b]
print(res)