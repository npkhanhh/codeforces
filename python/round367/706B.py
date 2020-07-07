from bisect import bisect_right

n = int(input())
a = sorted(map(int, input().split()))
for _ in range(int(input())):
    t = int(input())
    print(bisect_right(a, t))
