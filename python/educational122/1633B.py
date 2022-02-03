from sys import stdin

for _ in range(int(stdin.readline())):
    s = stdin.readline().strip()
    c = [0,0]
    for i in s:
        c[int(i)] += 1
    if c[0] == c[1]:
        print(c[0]-1)
    else:
        print(min(c))
