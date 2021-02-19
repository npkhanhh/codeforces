from sys import stdin


for _ in range(int(stdin.readline())):
    s_str, t = stdin.readline().split()
    ogs = int(s_str)
    s = list(map(int, list(s_str)))

    t = int(t)
    d= sum(s)
    if d <= t:
        print(0)
    else:
        diff = d-t +1
        i = len(s) - 1
        while diff > 0:
            diff -= s[i]
            i -= 1
        if i >= 0:
            ceil = (int(s_str[:i+1])+1) * (10**(len(s_str)-i-1))
        else:
            ceil = 10**len(s_str)
        print(int(ceil) - ogs)





