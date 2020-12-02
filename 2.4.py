num, sum = 1, 0
count = int(input("Введите натуральное число"))
while True:
    count -= 1
    sum += num
    num /= -2
    if count == 0:
        break
print(sum)

#https://app.diagrams.net/#G1EXxtPKfscDpntTgBZwsdeKWyq0S4lGyo