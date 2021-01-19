from sys import stdin

for _ in range(int(stdin.readline())):
    s = input()
    count = [0, 0]
    res = len(s)
    for i in s:
        count[int(i)] += 1
    encountered = [0, 0]
    for i in s:
        encountered[int(i)] += 1
        start_0 = encountered[0] + count[1] - encountered[1]
        start_1 = encountered[1] + count[0] - encountered[0]
        res = min([res, start_0, start_1])
    print(res)





