n = int(input())

group = 1
s = input()
t = s[-1]
for i in range(n-1):
    s = input()
    if t == s[0]:
        group += 1
    t = s[-1]

print(group)
