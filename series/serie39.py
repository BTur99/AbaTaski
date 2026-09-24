def is_chain(arr):
    c = 0
    for j in range(1, len(arr) - 1):
        if (arr[j] < arr[j + 1] and arr[j] < arr[j - 1]) or (arr[j] > arr[j + 1] and arr[j] > arr[j - 1]):
            c += 1        
    if c == len(arr) - 2:
        return True

try:
    k = int(input())
    m = []
    t = 0
    for i in range(k):
        m.append([])
        while 0 not in m[i]:
            m[i].append(int(input()))
        m[i].pop()
        if is_chain(m[i]):
            t += 1
            
    print(*m)
    print(t)
except:
    print("DUCKYOU")