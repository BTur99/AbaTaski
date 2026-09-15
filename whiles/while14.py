a = float(input())
s = 0
k = 1

while s < a:
    s += 1/k
    k += 1

if s >= a:
    k -= 1
    s -= 1/k
    
print(f"k = {k - 1}, sum = {s}")