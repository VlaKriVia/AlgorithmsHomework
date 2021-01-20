import math
import collections
import random

def merge(array, extra_array = collections.deque([])):
    print(extra_array)
    print(len(extra_array))
    if extra_array:
        new_array = collections.deque([])
        while 0 < len(array) and 0 < len(extra_array):
            if array[0] < extra_array[0]:
                new_array.append(extra_array.popleft())
            else: new_array.append(array.popleft())
        if array:
            new_array += array
        if extra_array:
            new_array += extra_array
        print("add", array, extra_array)
        return new_array
    elif len(array) == 1:
        print("tail", array, extra_array)
        return array
    else:
        half = math.floor(len(array) // 2)
        spam = collections.deque([])
        for i in range(half):
            spam.appendleft(array.popleft())
        print("div", array, spam)
        array, spam = merge(array), merge(spam)
        print("end")
        return merge(array, spam)


MIN_CONST = 0
MAX_CONST = 49
SIZE = 10

arr = collections.deque([random.randint(MIN_CONST, MAX_CONST) + random.random() for i in range(SIZE)])

print(merge(arr).reverse())