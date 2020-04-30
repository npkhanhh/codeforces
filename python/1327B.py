from sys import stdin

for _ in range(int(input())):
    n = int(input())
    prince = [False] * (n+1)
    princess = -1
    for i in range(n):
        b = [int(x) for x in stdin.readline().strip().split(" ")]
        married = False
        for j in b[1:]:
            if not prince[j]:
                prince[j] = True
                married = True
                break
        if not married:
            princess = i + 1
    if princess == -1:
        print('OPTIMAL')
    else:
        print('IMPROVE')
        res = -1
        for i in range(1, n+1):
            if not prince[i]:
                res = i
        print(princess, res)

