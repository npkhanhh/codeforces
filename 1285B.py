t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    adel = sum(l)
    max_start = max_end = -10**20
    max_start_temp = max_end_temp = 0
    for i in range(n-1):
        max_start_temp = max_start_temp + l[i]
        max_end_temp = max_end_temp + l[i + 1]
        if max_start < max_start_temp:
            max_start = max_start_temp
        if max_end < max_end_temp:
            max_end = max_end_temp

        if max_start_temp < 0:
            max_start_temp = 0
        if max_end_temp < 0:
            max_end_temp = 0
    print('YES' if adel > max_start and adel > max_end else 'NO')
