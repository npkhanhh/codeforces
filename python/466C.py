n = int(input())
a = list(map(int, input().split()))
total = sum(a)
if total % 3 != 0:
    print(0)
else:
    t = total // 3
    p = 0
    s = 0
    prefix = []
    suffix = []
    for idx, val in enumerate(a):
        j = n - idx - 1
        p += val
        s += a[j]

        if p == t:
            prefix.append(idx)
        if s == t:
            suffix.append(j)
    suffix = suffix[::-1]
    res = 0
    j = 0
    suffix_size = len(suffix)
    for idx, val in enumerate(prefix):
        while j < suffix_size and val >= suffix[j] - 1:
            j += 1
        res += suffix_size - j

    print(res)



