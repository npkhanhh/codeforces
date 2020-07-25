from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    has_other = False
    first_turn = True
    for i in a:
        if i == 1:
            first_turn = not first_turn
        else:
            has_other = True
            break
    if not has_other:
        first_turn = not first_turn
    print(['Second', 'First'][first_turn])


