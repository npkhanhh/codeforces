n = int(input())
a = list(map(int, input().split()))
s = sum(a)
m = max(a)
if s % 2 == 0 and m <= s // 2:
    print('YES')
else:
    print('NO')
