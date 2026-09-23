b = float(input())
n = int(input())
l = []
l.append(b)
for i in range(n):
    l.append(int(input()))
print(sorted(l))