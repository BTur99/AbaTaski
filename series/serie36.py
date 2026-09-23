def is_act(arr):
    l = arr
    r = False
    c = 0
    for j in range(len(l) - 1):
        if l[j] < l[j + 1]:
            c += 1
    if c == len(l) - 1:
        r = True
    return r
'''

k = int(input())
m = []
c = []
for i in range(k):
    m.append([])
    while 0 not in m[i]:
        m[i].append(int(input()))
    m[i].pop()

'''

# ! WORK IN PROCESS