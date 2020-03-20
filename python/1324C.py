for _ in range(int(input())):
    s = 'R' + input() + 'R'
    m = -1
    prev_s = 0
    for i, v in enumerate(s):
        if v == 'R':
            m = max(i-prev_s, m)
            prev_s = i
    print(m)

