from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    res = False
    for i in range(1, n-1):
        if a[i-1] < a[i] and a[i] > a[i+1]:
            print('YES')
            print(i, i+1, i+2)
            res = True
            break
    if res:
        continue
    print('NO')

