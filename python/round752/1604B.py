from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    res = 'NO'
    if n % 2 == 0:
        print('YES')
        continue
    for i in range(1, n):
        if a[i] <= a[i-1]:
            res = 'YES'
            break
    print(res)
