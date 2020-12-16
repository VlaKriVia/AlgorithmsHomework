#задача 3_3

import random

def func_1(size, min_value, max_value):
    size = int(size)
    min_value = int(min_value)
    max_value = int(max_value)
    array = [random.randint(min_value, max_value) for _ in range(size)]

    min_num = array[0]
    max_num = array[0]
    min_num_index = 0
    max_num_index = 0
    for count, i in enumerate(array):
        if i < min_num:
            min_num = i
            min_num_index = count
        elif i > max_num:
            max_num = i
            max_num_index = count
    array[min_num_index], array[max_num_index] = array[max_num_index], array[min_num_index]
    return array
#0.25141559999999996 print(timeit.timeit("func_1(100, 1, 100)", number=1000, globals=globals()))
#2.4875898           print(timeit.timeit("func_1(1000, 1, 100)", number=1000, globals=globals()))
#25.875367500000003  print(timeit.timeit("func_1(10000, 1, 100)", number=1000, globals=globals()))
'''   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.005    0.005    0.033    0.033 1.py:11(<listcomp>)
        1    0.002    0.002    0.034    0.034 1.py:7(func_1)
        1    0.000    0.000    0.034    0.034 <string>:1(<module>)
    10000    0.011    0.000    0.024    0.000 random.py:174(randrange)
    10000    0.004    0.000    0.028    0.000 random.py:218(randint)
    10000    0.009    0.000    0.013    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.034    0.034 {built-in method builtins.exec}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    12761    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
'''
#print(cProfile.run("func_1(10000, 1, 100)"))

def func_2(size, min_value, max_value):
    size = int(size)
    min_value = int(min_value)
    max_value = int(max_value)
    array = [random.randint(min_value, max_value) for _ in range(size)]

    min_num, max_num = array.index(min(array)), array.index(max(array))
    array[min_num], array[max_num] = array[max_num], array[min_num]
    return array
#0.2594532           print(timeit.timeit("func_2(100, 1, 100)", number=1000, globals=globals()))
#2.5461465999999997  print(timeit.timeit("func_2(1000, 1, 100)", number=1000, globals=globals()))
#25.1578683          print(timeit.timeit("func_2(10000, 1, 100)", number=1000, globals=globals()))
'''   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.033    0.033 1.py:30(func_2)
        1    0.005    0.005    0.033    0.033 1.py:34(<listcomp>)
        1    0.000    0.000    0.033    0.033 <string>:1(<module>)
    10000    0.011    0.000    0.023    0.000 random.py:174(randrange)
    10000    0.004    0.000    0.028    0.000 random.py:218(randint)
    10000    0.009    0.000    0.013    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.033    0.033 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    12723    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
        2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
'''
#print(cProfile.run("func_2(10000, 1, 100)"))

def func_3(size, min_value, max_value):
    size = int(size)
    min_value = int(min_value)
    max_value = int(max_value)
    array = [random.randint(min_value, max_value) for _ in range(size)]

    sort_array = array
    sort_array.sort()
    print(array)
    array[array.index(sort_array[0])], array[array.index(sort_array[-1])] = array[array.index(sort_array[-1])], array[array.index(sort_array[0])]
    print(array)
    return array
#0.23864580000000002 print(timeit.timeit("func_3(100, 1, 100)", number=1000, globals=globals()))
#2.4249476           print(timeit.timeit("func_3(1000, 1, 100)", number=1000, globals=globals()))
#24.33309            print(timeit.timeit("func_3(10000, 1, 100)", number=1000, globals=globals()))
'''   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.051    0.051 1.py:43(func_3)
        1    0.005    0.005    0.032    0.032 1.py:47(<listcomp>)
        1    0.000    0.000    0.051    0.051 <string>:1(<module>)
    10000    0.011    0.000    0.023    0.000 random.py:174(randrange)
    10000    0.004    0.000    0.028    0.000 random.py:218(randint)
    10000    0.009    0.000    0.013    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.052    0.052 {built-in method builtins.exec}
        2    0.018    0.009    0.018    0.009 {built-in method builtins.print}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    12808    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
        4    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
        1    0.001    0.001    0.001    0.001 {method 'sort' of 'list' objects}
'''
#print(cProfile.run("func_3(10000, 1, 100)"))