year = int(input("Введите год числом:"))
if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print("Год не високостный")
    else: print("Год високостный")
else: print("Год не високостный")

#https://app.diagrams.net/#G1snWl0-xEQ202YZlfd5tjJ_UKZsQQXRoO