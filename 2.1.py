while True:
    a, b = map(lambda x: int(x), input("Введите два числа").split())
    action = input("Введите желаемое действие одним символом ('0', '+', '-', '*', '/')")
    if action == "0":
        break
    elif action == "+":
        print(a+b)
    elif action == "-":
        print(a-b)
    elif action == "*":
        print(a*b)
    elif b != 0:
        print(a/b)
    else: print("Нельзя делить на ноль")

#https://app.diagrams.net/#G1nUZUE8SYCuqBlVtNUByhN_l2pVz_4fXR