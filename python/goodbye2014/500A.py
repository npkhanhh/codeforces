n, t = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))
s = 1
while s < t:
    s = s + a[s]
if s == t:
    print('YES')
else:
    print('NO')


