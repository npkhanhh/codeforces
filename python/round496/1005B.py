s1 = input().strip()
s2 = input().strip()
n1 = len(s1)
n2 = len(s2)
t = min(n1, n2)

for i in range(min(n1, n2)):
    if s1[-i - 1] != s2[-i - 1]:
        t = i
        break
print(n1 - t + n2 - t)
