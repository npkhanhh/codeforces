from sys import stdin



def sieve(size):
    sie = [-1] * size
    for i in range(2, int(size ** 0.5) + 1):
        if sie[i] != -1:
            continue
        for j in range(i * i, size, i):
            if sie[j] == -1:
                sie[j] = i
    return sie

s = sieve(50000)

for _ in range(int(stdin.readline())):
    d = int(stdin.readline())
    min_div = d + 1
    while s[min_div] != -1:
        min_div += 1
    sec_div = min_div + d

    while s[sec_div] != -1:
        sec_div += 1
    print(min_div*sec_div)
