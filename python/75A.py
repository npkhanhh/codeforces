a = input()
b = input()
c = int(a) + int(b)
aw = a.replace("0", "")
bw = b.replace("0", "")
cw = str(c).replace("0", "")
if int(aw) + int(bw) == int(cw):
    print('YES')
else:
    print('NO')
