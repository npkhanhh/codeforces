from sys import stdin
import random

n = int(stdin.readline())
a = []
groups = []
cur_group = 1
for i in range(n):
    x, y = list(map(int, stdin.readline().split()))
    new_group = set()
    for j in range(len(a)):
        if x == a[j][0] or y == a[j][1]:
            new_group.add(groups[j])
    a.append([x, y])
    if len(new_group) == 0:
        groups.append(cur_group)
        cur_group += 1
    elif len(new_group) >= 2:
        main = new_group.pop()
        for idx, val in enumerate(groups):
            if val in new_group:
                groups[idx] = main
        groups.append(main)
    else:
        groups.append(new_group.pop())
print(len(set(groups))-1)







