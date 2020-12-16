def func(n):
    n = int(n)
    count = 3
    a = [2]
    while len(a) < n:
        spam = True
        for j in a:
            if count % j == 0:
                spam = False
                break
        if spam:
            a.append(count)
        count += 1
    print(a[-1])

def func(n):
    n = int(n)
    a = [i for i in range(n**2)]
    a[1] = 0
    count = 2
    while count < n**2:
        if a[count] != 0:
            multiple_of_count = count * 2
            while multiple_of_count < n**2:
                a[multiple_of_count] = 0
                multiple_of_count = multiple_of_count + count
        count += 1
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    del a
    print(b[n-1])

