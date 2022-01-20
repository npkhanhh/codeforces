from sys import stdin

for _ in range(int(stdin.readline())):
    n = list(map(int, list(stdin.readline().strip())))
    cur_max = 0
    idx = -1
    for i in range(1, len(n)):
        if n[i] + n[i-1] >= 10:
            cur_max = n[i] + n[i-1]
            idx = i
    if idx > -1:
        res = n[:idx-1] + [cur_max//10] + [cur_max%10] + n[idx+1:]
    else:
        t = n[0] + n[1]
        res = [t] + n[2:]
    print(''.join(map(str, res)))
