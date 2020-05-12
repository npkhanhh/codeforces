n = int(input())
s = input().lower()
d = {}
for i in s:
    if i not in d:
        d[i] = True
print(['NO','YES'][len(d.keys()) == 26])
