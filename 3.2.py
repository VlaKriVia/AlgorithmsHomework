import random

SIZE = 20
MIN_VALUE = 1
MAX_VALUE = 100
array = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(SIZE)]
print(array)

new_array = []
for count, i in enumerate(array):
    if i % 2 == 0:
        new_array.append(count)
print(new_array)