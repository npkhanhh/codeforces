z = int(input())
for i in range(z):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    peaks = []
    start = end = -1
    res = 0
    res_end = 0
    j = -1
    count = 0
    for i in range(n-2, 0, -1):
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            peaks.append(i)
            if end == -1:
                end = i + 1
                count = 1
                j = 0
            elif end - (i - 1) >= k:
                if count >= res:
                    res = count
                    res_end = end
                count += 1
                while peaks[j] + 1 - (i - 1) >= k:
                    j += 1
                    count -= 1
                end = peaks[j] + 1
            elif end - (i - 1) < k:
                count += 1
    if count >= res:
        res = count
        res_end = end
    res_end = res_end - k + 2
    if res_end < 1:
        res_end = 1
    print(res + 1, res_end)
