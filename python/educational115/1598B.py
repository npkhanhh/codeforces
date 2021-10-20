from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = []
    for _ in range(n):
        a.append(list(map(int, stdin.readline().split())))
    res = 'NO'
    if n % 2 == 1:
        print(res)
        continue
    for i in range(4):
        for j in range(i+1, 5):
            first = 0
            second = 0
            both = 0
            for k in range(n):
                if a[k][i] == 1 and a[k][j] == 1:
                    both += 1
                elif a[k][i] == 1:
                    first += 1
                elif a[k][j] == 1:
                    second += 1
            if first > n//2 or second > n//2:
                continue
            elif first + second + both == n:
                res = 'YES'
                break
        if res == 'YES':
            break
    print(res)

