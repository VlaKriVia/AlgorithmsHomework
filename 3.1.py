for i in range(2, 10):
    count = 0
    for j in range(2, 100):
        if j % i == 0:
            count += 1
    print(f"Количество чисел в диапазоне от 2 до 99, которые являются кртными цифре {i}: {count}")
