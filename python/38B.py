
def build_str(r, c):
    return str(r) + str(c)

def knight_pos(r, c):
    res = []
    if r > 1 and c > 2:
        res.append(build_str(r-1, c-2))
    if r > 1 and c < 7:
        res.append(build_str(r-1, c+2))
    if r < 8 and c > 2:
        res.append(build_str(r+1, c-2))
    if r < 8 and c < 7:
        res.append(build_str(r+1, c+2))
    if r > 1 and c > 2:
        res.append(build_str(r-1, c-2))
    if r > 1 and c < 7:
        res.append(build_str(r-1, c+2))
    if r < 8 and c > 2:
        res.append(build_str(r+1, c-2))
    if r < 8 and c < 7:
        res.append(build_str(r+1, c+2))


r = input()
k = input()

c_r = ord(r[0]) - 96
r_r = int(r[1])

c_k = ord(k[0]) - 96
r_k = int(k[1])

d = dict(str(c_r)+str(r_r):True, )
res = 62


