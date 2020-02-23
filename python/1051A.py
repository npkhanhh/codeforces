for _ in range(int(input())):
    s = input()
    lower = upper = number = False
    for c in s:
        if c.islower():
            lower = True
        if c.isupper():
            upper = True
        if c.isdigit():
            number = True
    if all([lower, upper, number)]:
        print(s)
    else:
        

