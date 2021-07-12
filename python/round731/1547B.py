from sys import stdin

for _ in range(int(stdin.readline())):
    s = stdin.readline().strip()
    i = 0
    j = len(s) - 1
    res = True
    for idx in range(len(s) - 1, -1, -1):
        cur_char = chr(idx + 97)
        if s[i] == cur_char:
            i += 1
            continue
        if s[j] == cur_char:
            j -= 1
            continue
        res = False
        break
    print('YES' if res else 'NO')
