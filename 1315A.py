for _ in range(int(input())):
    a, b, x, y = list(map(int, input().split()))
    max_height = max(a - (x + 1), x)
    max_width = max(b - (y + 1), y)
    print(max(max_height*b, max_width*a))
