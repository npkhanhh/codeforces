d = [0, 3, 6, 1, 4, 7, 2, 5, 8]
for _ in range(int(input())):
    for i in range(9):
        s = list(input())
        t = int(s[d[i]]) + 1
        if t > 9:
            t = 1
        s[d[i]] = str(t)
        print(''.join(s))
