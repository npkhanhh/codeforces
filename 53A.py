s = input()
n = len(s)
a = []
for _ in range(int(input())):
    s1 = input()
    t = min(len(s1), n)
    if s1[:t] == s[:t]:
        a.append(s1)
    a = sorted(a)
if len(a) == 0:
    print(s)
else:
    print(a[0])

