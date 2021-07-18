from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(input())
    a = list(map(int, stdin.readline().split()))
    if sum(a) == 0:
        print('NO')
    else:
        print('YES')
        print(*sorted(a, reverse=sum(a)>0))
