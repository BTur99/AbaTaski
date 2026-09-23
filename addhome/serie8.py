n = int(input())
ch = ''
c = 0
for i in range(n):
    a = int(input())
    if a % 2 == 0:
        c += 1
        ch += str(a) + ' '
print(f"\n{c}\n{ch}")