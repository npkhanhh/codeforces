
d = {
    2: 3,
    3: 5,
    5: 7,
    7: 11,
    11: 13,
    13: 17,
    17: 19,
    19: 23,
    23: 29,
    29: 31,
    31: 37,
    37: 41,
    41: 43,
    43: 47
}

n, m = list(map(int, input().split()))
if n in d and d[n] == m:
    print('YES')
else:
    print('NO')
