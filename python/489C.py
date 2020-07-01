m, s = list(map(int, input().split()))
if 9 * m < s or (s == 0 and m > 1):
    print(-1, -1)
elif s == 0 and m == 1:
    print(0, 0)
else:
    x, y = divmod(s, 9)
    postfix = ''
    if y != 0:
        postfix = str(y)
    biggest = '9' * x + postfix + (m - x - len(postfix)) * '0'
    smallest = biggest[::-1]
    if m - x - len(postfix) > 0:
        if y > 0:
            y -= 1
            smallest = '1' + '0' * (m - x - 2) + str(y) + '9' * x
        else:
            smallest = '1' + '0' * (m - x - 2) + '08' + '9' * (x - 1)
    print(smallest, biggest)
