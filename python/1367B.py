from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    count_odd = 0
    count_even = 0
    for idx, val in enumerate(a):
        if val % 2 != idx % 2:
            if val % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    if count_even == count_odd:
        print(count_even)
    else:
        print(-1)

