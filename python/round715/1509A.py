from sys import stdin

for _ in range(int(stdin.readline())):
    input()
    a = list(map(int, stdin.readline().split()))
    odds = []
    evens = []
    for i in a:
        if i % 2 == 1:
            odds.append(i)
        else:
            evens.append(i)
    print(*(odds+evens))
