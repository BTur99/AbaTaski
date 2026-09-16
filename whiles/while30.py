a, b, c = map(int, input().split())
h = a
h2 = b
count = 0

while h >= c:
    h -= c
    while h2 >= c:
        count += 1
        h2 -= c

print(count)