s = input()
t = input()

res = 1

for idx, c in enumerate(t):
    if s[res-1] == c:
        res += 1

print(res)
