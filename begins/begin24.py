A = input("A: ") 
B = input("B: ")
C = input("C: ")

help = C
help2 = B
C = A
B = help
A = help2
print(f"\nA = {A}\nB = {B}\nC = {C}")