s = input()
n = len(s)
c = 0
for i in range(n//2):
    if s[i] != s[-i-1]:
        c += 1
if c > 1:
    print('NO')
if c == 1:
    print('YES')
if c == 0:
    if n % 2 == 1:
        print('YES')
    else:
        print('NO')


