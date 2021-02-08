import queue
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
mem = {}
q = queue.Queue()
for idx, val in enumerate(a):
    if q.qsize() < k and val not in mem:
        mem[val] = True
        q.put(val)
    else:
        if val not in mem or not mem[val]:
            q.put(val)
            mem[val] = True
            popped_element = q.get()
            mem[popped_element] = False
res = list(q.queue)[::-1]
print(len(res))
print(*res)

