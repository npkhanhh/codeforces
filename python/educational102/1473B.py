from sys import stdin
import math

for _ in range(int(stdin.readline())):
    s1 = stdin.readline().strip()
    s2 = stdin.readline().strip()
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    l1 = len(s1)
    l2 = len(s2)
    g = math.gcd(l1, l2)
    r1 = l1 // g
    r2 = l2 // g
    u1 = s1[:g]
    u2 = s2[:g]
    if u1 == u2 and u1*r1 == s1 and u2*r2 == s2:
        lcm = (l1*l2)//g
        print(s1 * (lcm // l1))

    else:
        print(-1)

