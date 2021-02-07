from sys import stdin

for _ in range(int(stdin.readline())):
    a = list(map(int, stdin.readline().split()))
    s = sum(a)
    m = min(a)
    if s % 9 == 0 and m >= s // 9:
        print('YES')
    else:
        print('NO')



