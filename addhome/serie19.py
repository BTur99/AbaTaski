n = int(input())
l = []
k = 0
kh = ''
for i in range(n):
    l.append(int(input()))
for j in range(len(l) - 1):
    if l[j + 1] < l[j]:
        k += 1
        kh += str(l[j + 1]) + " "
print(f"\n{k}\n{kh}")