from sys import stdin

for _ in range(int(stdin.readline())):
    s = sorted(list(stdin.readline().strip()))
    direction = 0
    res = 'Yes'
    for i in range(1, len(s)):
        cur = ord(s[i]) - ord(s[i-1])
        if cur != 1:
            res = 'No'
            break
    print(res)
