import random

SIZE = 20
MIN_VALUE = 1
MAX_VALUE = 100
array = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(SIZE)]
print(array)

min_num = array[0]
second_min_num = array[0]
for i in array:
    if i < min_num:
        second_min_num = min_num
        min_num = i
    elif i < second_min_num:
        second_min_num = i
print(f"Минимальное число в массиве: {min_num} \n"
      f"Второе минимальное число в массиве: {second_min_num}")