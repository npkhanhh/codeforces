from sys import stdin

for _ in range(int(stdin.readline())):
    a, b = sorted(map(int, stdin.readline().split()))
    if a <= b // 3:
        print(a)
    else:
        print((a+b)//4)
