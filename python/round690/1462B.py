from sys import stdin

ss = '2020'

for _ in range(int(stdin.readline())):
    stdin.readline()
    s = stdin.readline().rstrip()
    i = j = 0
    while j < 4 and s[i] == ss[j]:
        i += 1
        j += 1
    res = "NO"
    if j == 4 or ss[j:] == s[-(4-i):]:
        res = "YES"
    print(res)



