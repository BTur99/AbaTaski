try:
    n = int(input())
    s = 0
    sm = ''
    for i in range(n):
        a = float(input())
        a -= int(a)
        s += a
        sm += str(a) + ' '
    print(f"\n{s}\n{sm}")
except:
    print("DUCKYOU")