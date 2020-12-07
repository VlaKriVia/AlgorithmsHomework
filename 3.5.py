import random

SIZE = 20
MIN_VALUE = -50
MAX_VALUE = 50
array = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(SIZE)]
print(array)

max_negative_num = array[0]
for i in array:
    if 0 <= max_negative_num or max_negative_num < i < 0:
        max_negative_num = i

print(f"Минимальное отрицательное число в массиве: {max_negative_num}")