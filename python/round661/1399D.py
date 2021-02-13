from sys import stdin

for _ in range(int(stdin.readline())):
    stdin.readline()
    s = stdin.readline().strip()
    one_stack = []
    z_stack = []
    count = 0
    res = []
    for char in s:
        if char == '1':
            if len(z_stack) == 0:
                count += 1
                res.append(count)
                one_stack.append(count)
            else:
                t = z_stack.pop()
                res.append(t)
                one_stack.append(t)
        else:
            if len(one_stack) == 0:
                count += 1
                res.append(count)
                z_stack.append(count)
            else:
                t = one_stack.pop()
                res.append(t)
                z_stack.append(t)
    print(count)
    print(*res)
