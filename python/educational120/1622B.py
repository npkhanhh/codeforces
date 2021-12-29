from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    p = list(map(int, stdin.readline().split()))
    s = stdin.readline().strip()
    like, dislike = [], []
    for idx, val in enumerate(p):
        if s[idx] == '1':
            like.append((idx, val))
        else:
            dislike.append((idx, val))
    like = sorted(like, key=lambda x: x[1])
    dislike = sorted(dislike, key=lambda x: x[1])
    res = [0] * n
    for i in range(1, n + 1):
        idx = i - 1
        if idx < len(dislike):
            res[dislike[idx][0]] = i
        else:
            res[like[idx - len(dislike)][0]] = i
    print(*res)
