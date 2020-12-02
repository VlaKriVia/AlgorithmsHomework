def reverse(num, new_num):
    print(num, new_num)
    if num == 0:
        return new_num
    else: return reverse(num // 10, num % 10 + new_num * 10)

num = int(input("Введите натуральное число"))
new_num = reverse(num, 0)
print(new_num)

#https://app.diagrams.net/#G1JTkWj96Ue9AJCGrcjL2x5g3wcA-473NT