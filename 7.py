a, b, c = map(lambda x: int(x), input("Введите длины трёх отрезков: ").split())
if a + b > c or b + c > a or a + c > b:
    print("Такого треугольника несуществует")
elif a == b and b == c:
    print("Этот треугольник равносторонний")
elif a == b or b == c or c == a:
    print("Этот треугольник равнобедренный")
else: print("Этот треугольник разносторонний")

#https://app.diagrams.net/#G1oziBz86jKGhF3-1zK5qzElKJeX1LtqyZ