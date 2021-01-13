import sys
import random
import collections

def get_all_sizes(array):
    size_sum = 0
    for i in array:
        size_sum += sys.getsizeof(i)
        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, collections.deque):
            size_sum += get_all_sizes(i)
    return size_sum

#------------------------------------------------------------------------------------

SIZE = 20
MIN_VALUE = 1
MAX_VALUE = 100
array = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(SIZE)]
print(array)

min_num = array[0]
max_num = array[0]
for i in array:
    if i < min_num:
        min_num = i
    elif i > max_num:
        max_num = i
array[array.index(min_num)], array[array.index(max_num)] = array[array.index(max_num)], array[array.index(min_num)]
print(f"Минимальное число в массиве: {min_num} \n"
      f"Максимальное число в массиве: {max_num}")

print(get_all_sizes([SIZE, MIN_VALUE, MAX_VALUE, array, min_num, max_num, array[-1]]))

#------------------------------------------------------------------------------------

SIZE = 20
MIN_VALUE = 1
MAX_VALUE = 100
array = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(SIZE)]
print(array)

array[array.index(min(array))], array[array.index(max(array))] = array[array.index(max(array))], array[array.index(min(array))]
print(f"Минимальное число в массиве: {min(array)} \n"
      f"Максимальное число в массиве: {max(array)}")

print(get_all_sizes([SIZE, MIN_VALUE, MAX_VALUE, array]))

#------------------------------------------------------------------------------------

SIZE = 20
MIN_VALUE = 1
MAX_VALUE = 100
array = collections.deque([random.randint(MIN_VALUE, MAX_VALUE) for _ in range(SIZE)])
print(array)

min_num = array[0]
max_num = array[0]
for i in array:
    if i < min_num:
        min_num = i
    elif i > max_num:
        max_num = i
array[array.index(min_num)], array[array.index(max_num)] = array[array.index(max_num)], array[array.index(min_num)]
print(f"Минимальное число в массиве: {min_num} \n"
      f"Максимальное число в массиве: {max_num}")

print(get_all_sizes([SIZE, MIN_VALUE, MAX_VALUE, array, min_num, max_num, array[-1]]))

#------------------------------------------------------------------------------------

"""
Вариант номер один изачальный, и он же хуже всех, как по памяти, так и по времени исполнения.
Вариант номер три быстрее, но занимает больше места.
Вариант два оптимален, так как не использует переменных, и использует функции.
Версия ОС - Microsoft Windows 10 Pro
Разядность - 64
Версия Python - 3.9.1
"""