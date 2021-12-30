from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    s = set()
    for i in a:
        if i not in s:
            s.add(i)
        else:
            s.add(-i)
    print(len(s))
