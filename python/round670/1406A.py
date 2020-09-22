from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = sorted(map(int, stdin.readline().split()))
    mex_a, mex_b = 0, 0
    for i in a:
        if i == mex_a:
            mex_a += 1
        elif i == mex_b:
            mex_b += 1

    print(mex_a + mex_b)
