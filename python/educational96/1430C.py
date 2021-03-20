from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    t = n
    print(2)
    if n == 2:
        print(1, 2)
    else:
        for i in range(t-2):
            print(n, n-2)
            if i ==0:
                print(n-1, n-1)
            n -= 1
