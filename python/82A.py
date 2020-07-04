import math
n = int(input())
k = math.floor(math.log2((n + 5) // 5))
start = (2**k-1)*5+1
end = (2**(k+1)-1)*5
print(['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard'][math.floor((n - start)/(end-start+1)*5)])

