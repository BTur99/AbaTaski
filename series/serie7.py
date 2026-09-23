try:
    n = int(input())
    s = 0
    sm = ''
    for i in range(n):
        a = float(input())
        s += round(a)
        sm += str(round(a)) + ' '
    print(f"\n{s}\n{sm}")
except:
    print("DUCKYOU")