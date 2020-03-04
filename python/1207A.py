for _ in range(int(input())):
    b, p, f = list(map(int, input().split()))
    h, c = list(map(int, input().split()))
    no_burger = min(b//2, p+f)
    if no_burger == 0:
        print(0)
    elif c > h:
        if no_burger > f:
            print(f*c + h*(no_burger-f))
        else:
            print(no_burger*c)
    else:
        if no_burger > p:
            print(p*h +c*(no_burger-p))
        else:
            print(no_burger*h)