from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    res = 'Yes'
    for i in range(n-1):
        if a[i+1] > a[i] + 1:
            res = 'No'
            break
    print(res)


