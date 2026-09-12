from sys import exit

a = int(input())
b = int(input())

if a == 0 or b == 0:
    exit(1)

mod_a = abs(a)
mod_b = abs(b)

print(f"sum = {mod_a + mod_b}\nsumod_b = {mod_a - mod_b}\nmult = {mod_a * mod_b}\ndiv = {mod_a / mod_b}")