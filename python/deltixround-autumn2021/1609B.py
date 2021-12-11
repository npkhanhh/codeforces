from sys import stdin

n, q = list(map(int, stdin.readline().split()))
s = list(stdin.readline().strip())
count = 0
m = [False] * n
for i in range(n - 2):
    if s[i] == 'a' and s[i + 1] == 'b' and s[i + 2] == 'c':
        count += 1
        m[i] = True

for _ in range(q):
    i, c = stdin.readline().split()
    i = int(i) - 1
    if s[i] == c:
        print(count)
        continue
    for j in range(i - 2, i + 1):
        if j < 0 or j >= n-2:
            continue
        if s[j] == 'a' and s[j + 1] == 'b' and s[j + 2] == 'c':
            count -= 1
            m[j] = False
    s[i] = c
    for j in range(i - 2, i + 1):
        if j < 0 or j >= n-2:
            continue
        if s[j] == 'a' and s[j + 1] == 'b' and s[j + 2] == 'c':
            count += 1
            m[j] = True
    print(count)
