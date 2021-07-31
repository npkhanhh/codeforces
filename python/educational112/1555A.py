from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n % 2 == 1:
        n += 1
    res = 15
    t = max(0, n-6)
    res += t//2 * 5
    print(res)
