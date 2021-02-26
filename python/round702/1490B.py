from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    t = n // 3
    a = list(map(int, stdin.readline().split()))
    res = 0
    b = [0, 0, 0]
    for i in a:
        b[i % 3] += 1
    for i in range(3):
        c = i % 3
        if b[c] > t:
            diff = b[c] - t
            if b[(c+1)%3] < t:
                move_1 = min(diff, t - b[(c+1)%3])
                res += move_1
                b[c] -= move_1
                diff -= move_1
                b[(c+1)%3] += move_1
            if b[(c+2)%3] < t:
                move_2 = min(diff, t - b[(c+2)%3])
                res += 2 * move_2
                b[c] -= move_2
                diff -= move_2
                b[(c+2)%3] += move_2
    print(res)
