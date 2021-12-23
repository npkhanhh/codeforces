from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    t = n - 1
    if t % 2 == 1:
        print(t//2+1, t//2, 1)
    else:
        t = t//2
        if t % 2 == 1:
            print(t+2, t-2, 1)
        else:
            print(t+1, t-1, 1)
