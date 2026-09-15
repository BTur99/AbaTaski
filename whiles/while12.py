n = int(input())
s = 0
k = 0

while s < n:
    s += k
    k += 1

if s > n:
    s -= (k - 1)
    k -= 1
    
print(f"k = {k - 1}, sum = {s}")