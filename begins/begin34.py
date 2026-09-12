x, a = input().split()
y, b = input().split()

sum_kg_x = int(x)/int(a)
sum_kg_y = int(y)/int(b)
dif = abs(sum_kg_x - sum_kg_y)

print(f"За 1 кг x: {sum_kg_x}\nЗа 1 кг y: {sum_kg_y}\nРазность: {dif}")
