from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = sorted(map(int, stdin.readline().split()), reverse=True)
    alice, bob = 0, 0
    for idx, val in enumerate(a):
        if idx % 2 == 0 and val % 2 == 0:
            alice += val
        elif idx % 2 == 1 and val % 2 == 1:
            bob += val
    if alice > bob:
        print("Alice")
    elif bob > alice:
        print("Bob")
    else:
        print("Tie")

