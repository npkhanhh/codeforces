from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, list(stdin.readline().rstrip())))
    has_odd_in_odd, has_even_in_even = False, False
    for idx, val in enumerate(a):
        if val % 2 == 1 and (idx + 1) % 2 == 1:
            has_odd_in_odd = True
        if val % 2 == 0 and (idx + 1) % 2 == 0:
            has_even_in_even = True
    if (n % 2 == 1 and has_odd_in_odd) or (n % 2 == 0 and not has_even_in_even):
        print(1)
    else:
        print(2)
