from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    res = ''
    for i in range(n):
        res += chr(i%k + 97)
    print(res)
