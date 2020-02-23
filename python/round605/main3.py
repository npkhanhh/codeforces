n, k = list(map(int, input().split()))

s = input()

c = input().split()

r = 0
t = 0
for i in range(n):
    if s[i] not in c:
        r += (t * (t + 1)) / 2
        t = 0
    else:
        t += 1
r += (t * (t + 1)) / 2
print(int(r))
