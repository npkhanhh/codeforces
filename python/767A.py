n = int(input())
a = list(map(int, input().split()))
t = [False]*n
t_idx = n-1
for idx, value in enumerate(a):
    t[value-1] = True
    cur_res = []
    while t[t_idx]:
        cur_res.append(t_idx+1)
        t_idx -= 1
        if t_idx == -1:
            break
    print(*cur_res)

