n = int(input())


home = []
away = {}
for _ in range(n):
    s = list(map(int, input().split()))

    home.append(s[0])
    if s[1] not in away:
        away[s[1]] = 1
    else:
        away[s[1]] += 1
res = 0
for i in home:
    if i in away:
        res += away[i]
print(res)
