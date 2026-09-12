A = input("A: ") 
B = input("B: ")
C = input("C: ")

help = B
help2 = C
B = A
C = help
A = help2
print(f"\nA = {A}\nB = {B}\nC = {C}")