try:
    n = int(input("Enter: "))
    r = ''
    l = []

    for k in range(n):
        l.append(float(input()))
        
        
    for i in range(len(l)):
        c = n
        for j in range(n):
            r += str((l[i])**(c)) + ' '
            c -= 1
        r += "\n"
        
    print(r)
except:
    print("DUCKYOU")