import random
import collections
import math

m = int(input())
MIN_CONST = -100
MAX_CONST = 99
SIZE = m * 2 + 1
arr = [random.randint(MIN_CONST, MAX_CONST) for i in range(SIZE)]

half_arr = math.floor(len(arr) // 2)
less_arr = collections.deque()

while len(less_arr) - 1 < half_arr:
    min = math.inf
    count = 1
    for i in arr:
        if i < min and i not in less_arr:
            min = i
        elif i == min and i not in less_arr:
            count += 1
    print([min] * count)
    less_arr.extend([min] * count)

print(less_arr[-1])