from sys import stdin

for _ in range(int(stdin.readline())):
    l, r, k = list(map(int, stdin.readline().split()))
    if k == 0 and l == r and l != 1:
        print('YES')
        continue
    if l % 2 == 0:
        l += 1
    if r % 2 == 0:
        r -= 1
    c = (r-l) // 2 + 1
    print('NO' if c > k else 'YES')
