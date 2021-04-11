from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    while n%2 ==0:
        n //= 2
    if n == 1:
        print('NO')
    else:
        print('YES')
