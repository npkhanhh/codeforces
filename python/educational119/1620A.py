from sys import stdin

for _ in range(int(stdin.readline())):
    s = stdin.readline().strip()
    count_n = 0
    for i in s:
        if i == 'N':
            count_n += 1
    print('NO' if count_n == 1 else 'YES')
