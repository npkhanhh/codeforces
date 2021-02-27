from sys import stdin
import bisect

n, m = list(map(int, stdin.readline().split()))
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))
p_a = [0]*n
p_a[0] = a[0]
for i in range(1, n):
    p_a[i] = a[i] + p_a[i-1]
p_a = [0]+p_a
for i in b:
    dorm = bisect.bisect(p_a, i)
    room = i - p_a[dorm-1]
    if room == 0:
        dorm -= 1
        room = a[dorm-1]
    print(dorm, room)


