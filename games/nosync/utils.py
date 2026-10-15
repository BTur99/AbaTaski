import random

def create_exesice():
    nums = []
    zn = random.choice(["-", "+", "*"])
    for _ in range(2):
        nums.append(random.randint(-20, 20))

    if nums[1] < 0:
        exersice = f"{nums[0]} {zn} ({nums[1]})"
    else:
        exersice = f"{nums[0]} {zn} {nums[1]}"

    if zn == "-":
        result = nums[0] - nums[1]
    elif zn == "+":
        result = nums[0] + nums[1]
    elif zn == "*":
        result = nums[0] * nums[1]

    return exersice, result

