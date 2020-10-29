from sys import stdin

a = [1, 3, 6, 10]
for _ in range(int(stdin.readline())):
    s = stdin.readline().rstrip()
    t = len(s) - 1
    c = int(s[0]) - 1
    print(c*10 + a[t])


