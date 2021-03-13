from sys import stdin



n = int(stdin.readline())
s = stdin.readline().strip()
diag_char = s[0]
other_char = s[1]
i = 0
res = diag_char != other_char
a = i
b = n - i - 1
for j in range(n):
    if j == a or j == b:
        if s[j] != diag_char:
            res = False
    else:
        if s[j] != other_char:
            res = False
i += 1
for _ in range(n-1):
    s = stdin.readline().strip()
    a = i
    b = n - i - 1
    for j in range(n):
        if j == a or j == b:
            if s[j] != diag_char:
                res = False
        else:
            if s[j] != other_char:
                res = False
    i += 1
print('YES' if res else 'NO')


