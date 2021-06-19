from sys import stdin


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    res = 'Bob'
    if n % 2 == 0:
        res = 'Alice'
    for i in range(1, 31, 2):
        if pow(2, i) == n:
            res = 'Bob'

    print(res)
