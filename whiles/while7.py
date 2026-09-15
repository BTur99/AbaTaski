n = int(input())
k = 0


while k**2 < n:
    k += 1
    
if k**2 <= n:
    k += 1
    
print(k, k**2)