import random

def bubble(array):
    for j in range(1, len(array)):
        for i in range(len(array) - j):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array


MIN_CONST = -100
MAX_CONST = 99
SIZE = 10

arr = [random.randint(MIN_CONST, MAX_CONST) for i in range(SIZE)]

print(arr)
print(bubble(arr))