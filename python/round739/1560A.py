from sys import stdin

a = [0]*1000

t = 1
for i in range(1000):
    while t % 3 == 0 or t % 10 == 3:
        t += 1
    a[i] = t
    t+= 1

for _ in range(int(stdin.readline())):
    print(a[int(stdin.readline()) -1])
