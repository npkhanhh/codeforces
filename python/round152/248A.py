from sys import stdin

n = int(stdin.readline())
count = [0, 0]
for _ in range(n):
    a, b = list(map(int, stdin.readline().split()))
    if a == 0:
        count[0] += 1
    if b == 0:
        count[1] += 1
print(min(n-count[0], count[0]) + min(n-count[1], count[1]))
