def is_chain(arr):
    c = 0
    for j in range(1, len(arr) - 1):
        if (arr[j] < arr[j + 1] and arr[j] < arr[j - 1]) or (arr[j] > arr[j + 1] and arr[j] > arr[j - 1]):
            c += 1        
    if c == len(arr) - 2:
        return len(arr)
    else:
        if j != 0 and j != len(arr):
            return j + 1

try:
    k = int(input())
    m = []
    t = []
    for i in range(k):
        m.append([])
        while 0 not in m[i]:
            m[i].append(int(input()))
        m[i].pop()
        t.append(is_chain(m[i]))
            
    print(*m)
    print(*t)
except:
    print("DUCKYOU")