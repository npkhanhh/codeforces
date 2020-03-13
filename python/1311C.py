for _ in range(int(input())):
    res = [0]*26
    n, m = list(map(int, input().split()))
    s = input()
    a = sorted(list(map(int, input().split())))
    a.append(n)
    j = 0
    for i, v in enumerate(s):
        while j <= m and a[j] - 1 < i:
            j += 1
        res[ord(v)-97] += m - j + 1
    print(*res)
