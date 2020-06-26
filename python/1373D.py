from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    res = 0
    max_so_far_before = 0
    max_ending_before = 0
    max_so_far_after = 0
    max_ending_after = 0
    for i, v in enumerate(a):
        if i % 2 == 0:
            res += v
        else:
            max_ending_before += v - a[i-1]
            if max_ending_before < 0:
                max_ending_before = 0
            if max_so_far_before < max_ending_before:
                max_so_far_before = max_ending_before
            if i < n - 1:
                max_ending_after += v - a[i+1]
                if max_ending_after < 0:
                    max_ending_after = 0
                if max_so_far_after < max_ending_after:
                    max_so_far_after = max_ending_after
    res += max(max_so_far_after, max_so_far_before)
    print(res)

