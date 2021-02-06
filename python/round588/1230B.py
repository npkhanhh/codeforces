n, k = list(map(int, input().split()))
s = input()
t = '1'+'0'*(n-1)
change = 0
to = 0
for idx, val in enumerate(s):
    if change == k:
        break
    if val != t[idx]:
        change += 1
        to = idx + 1
if n == 1 and k == 0:
    print(s)
elif n == 1 and k> 0:
    print(0)
elif change < k:
    print(t)
else:
    print(t[:to] + s[to:])
