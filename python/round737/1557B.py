from sys import stdin
import bisect

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    b = sorted(a)
    cur = 1
    cur_idx = bisect.bisect_left(b, a[0])
    for i in range(1, n):
        if cur_idx+1 == n or a[i] != b[cur_idx+1]:
            cur += 1
            cur_idx = bisect.bisect_left(b, a[i])
            if cur > k:
                break
        else:
            cur_idx+=1
    if cur <= k:
        print('Yes')
    else:
        print('No')


