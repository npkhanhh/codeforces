from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    if sum(a) != sum(b):
        print(-1)
    else:
        res = []
        a_smaller = []
        for i in range(n):
            if a[i] < b[i]:
                a_smaller.append(i)
        j = 0
        for i in range(n):
            while a[i] > b[i]:
                a[i] -= 1
                a[a_smaller[j]] += 1
                res.append((i+1, a_smaller[j]+1))
                if a[a_smaller[j]] == b[a_smaller[j]]:
                    j += 1
        print(len(res))
        for ele in res:
            print(*ele)

