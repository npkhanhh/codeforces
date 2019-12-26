input()

s = input()
count_a = count_d = 0
for i in s:
    if i == 'A':
        count_a+=1
    else:
        count_d+=1
if count_a > count_d:
    print('Anton')
elif count_a < count_d:
    print('Danik')
else:
    print('Friendship')
