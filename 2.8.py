count = 0
num, digit = map(lambda x: int(x), input("Введите натуральное число и цифру от 1 до 10").split())
while True:
    if num % 10 == digit:
        count += 1
    num //= 10
    if num == 0:
        break
print(count)

#https://app.diagrams.net/#G1x3lnV9y6nZ5A1mpWKE_cIWeGJ7AN4lMv