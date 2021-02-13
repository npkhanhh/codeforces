#TODO: python3 submission
from sys import stdin

for _ in range(int(stdin.readline())):
    s = stdin.readline().strip()
    max_len = 0
    for i in range(10):
        for j in range(10):
            idx = 0
            cur_len = 0
            for char in s:
                if int(char) == i and cur_len % 2 == 0:
                    cur_len += 1
                elif int(char) == j and cur_len % 2 == 1:
                    cur_len += 1
            if i != j and cur_len % 2 == 1:
                cur_len -= 1
            max_len = max(cur_len, max_len)

    print(len(s) - max_len)


def solve(ss):
    aa = [0] * 100
    for i in map(int, ss[:-1]):
        for j in range(10):
            aa[10 * i + j] = aa[10 * j + i] + 1
    print(aa)
    print(len(ss) - 1 - max(max(aa) & ~1, *aa[::11]))
