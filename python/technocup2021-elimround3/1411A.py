from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    s = stdin.readline().strip()
    i = n-1
    while i >= 0 and s[i] == ')':
        i -= 1
    if (n-i-1) > (i+1):
        print('Yes')
    else:
        print('No')
