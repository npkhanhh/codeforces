from sys import stdin

for _ in range(int(input())):
    res = 'YES'
    a, b = list(map(int, stdin.readline().split()))
    if a <= 3 and b > a:
        if a != 2 or b != 3:
            res = 'NO'
    print(res)
