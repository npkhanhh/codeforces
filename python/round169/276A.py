from sys import stdin

a = []

n, k = list(map(int, stdin.readline().split()))
for _ in range(int(n)):
    f, t = list(map(int, stdin.readline().split()))
    if t > k:
        a.append(f - (t - k))
    else:
        a.append(f)
print(sorted(a)[-1])
