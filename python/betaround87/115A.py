from sys import stdin


class Node:
    def __init__(self):
        self.val = 1
        self.parent = None


n = int(stdin.readline())
a = [Node() for _ in range(n)]
res = 1
for i in range(n):
    t = int(stdin.readline())
    if t != -1:
        a[i].parent = a[t - 1]
        a[i].val = a[t - 1].val + 1
        res = max(res, a[i].val)
changed = True
while changed:
    changed = False
    for i in range(n):
        if a[i].parent is not None and a[i].val != a[i].parent.val + 1:
            a[i].val = a[i].parent.val + 1
            res = max(res, a[i].val)
            changed = True
print(res)
