from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, input().split()))
    even = []
    odd = []
    for idx, val in enumerate(a):
        if val % 2 == 0:
            even.append(idx + 1)
        else:
            odd.append(idx + 1)
    if len(even) % 2 == 1:
        even = even[1:]
        odd = odd[1:]
    else:
        if len(even) >= 2:
            even = even[2:]
        elif len(odd) >= 2:
            odd = odd[2:]
    for i in range(len(even)-1, -1, -2):
        print(even[i], even[i-1])
    for i in range(0, len(odd), 2):
        print(odd[i], odd[i+1])
