n = int(input())
t = 0
s = 0
while s < n:
    t += 1
    s += t*(t + 1) // 2
if s == n:
    print(t)
else:
    print(t-1)
