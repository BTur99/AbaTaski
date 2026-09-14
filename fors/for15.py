a = float(input())
n = int(input())
h = a

if n <= 0:
    exit(1)
    
for i in range(n - 1):
    a *= h

print(a)
