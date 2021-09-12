from sys import stdin


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    num_z = n - 2
    a = [1, 1] + [0]*num_z
    for i in range(n):
        print(*a)
        a.append(a[0])
        a = a[1:]

