
def cal_cell(h, w, r, c):
    res = 0
    for index, value in enumerate(r):
        t = value
        if value < w:
            t += 1
        for j in range(w):
            if j < value and c[j] == index:
                return -1
            if j == value and c[j] > index:
                return -1
            if j > value and c[j] >= index:
                t += 1
        left = w - t
        if left < 0:
            return -1
        res += left
    return res



h, w = list(map(int, input().split()))
r = list(map(int,input().split()))
c = list(map(int,input().split()))

cell = cal_cell(h, w, r, c)
if cell == -1:
    print(0)
else:
    print(int(pow(2, cell, 1000000007)))




