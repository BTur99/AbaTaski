n = int(input())
k = 0

while 3**k < n:
    k += 1

if 3**k >= n:
    k -= 1

print(k, 3**k)