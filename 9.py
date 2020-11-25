a, b, c = map(lambda x: int(x), input("Введите три разных числа").split())
if a < b:
    if b < c:
        if a < b:
            print("Второе число находится по середине")
        else:
            print("Первое число находится по середине")
    else:
        if a < c:
            print("Третье число находится по середине")
        else:
            print("Первое число находится по середине")
else:
    if a < c:
        if a < b:
            print("Второе число находится по середине")
        else:
            print("Первое число находится по середине")
    else:
        if b < c:
            print("Второе число находится по середине")
        else:
            print("Третье число находится по середине")

#https://app.diagrams.net/#G11TlidKt-HDvTeut4Pc7ihJq307DHg0Gq