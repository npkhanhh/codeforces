from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = sorted(enumerate(map(int, stdin.readline().split())), key=lambda x: x[1], reverse=True)
    tot = 0
    res = [0]*(n+1)
    distance = 1
    for i in a:
        res[i[0]+1] = distance
        tot += i[1]*2*abs(distance)
        distance = -distance
        if distance > 0:
            distance += 1

    print(tot)
    print(*res)
