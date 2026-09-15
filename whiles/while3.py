n = int(input())
k = int(input())
count = 0


while k <= n:
    count += 1
    if k <= (n - k):
        n -= k
    else:
        break
    

print(f"{count} ost({n - k})")