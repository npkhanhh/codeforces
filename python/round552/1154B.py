from sys import stdin
from collections import Counter

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
d = dict(Counter(a))
if len(d) > 3:
    print(-1)
else:
    val = sorted(d.keys())
    if len(val) == 1:
        print(0)
    elif len(val) == 2:
        diff = val[1] - val[0]
        if diff % 2 == 0:
            print(diff // 2)
        else:
            print(diff)
    else:
        diff1 = val[1] - val[0]
        diff2 = val[2] - val[1]
        if diff1 != diff2:
            print(-1)
        else:
            print(diff1)



