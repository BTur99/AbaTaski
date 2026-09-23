k, n = map(int, input().split())
r = False

for i in range(n):
    a = int(input())
    if a < k:
        r = True
print(r)