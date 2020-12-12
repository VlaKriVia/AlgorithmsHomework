def count_odd_even(num, even, odd):
    if num == 0:
        return even, odd
    elif num % 10 % 2 == 0:
        return count_odd_even(num // 10, even + 1, odd)
    else: return count_odd_even(num // 10, even, odd + 1)

num = int(input("Введите натуральное число"))
even, odd = count_odd_even(num, 0, 0)
print(f"{even} чётных чисел, {odd} нечётных чисел")

#https://app.diagrams.net/#G1hl8-O37vJWXEWqiHWWGB3Xv-S1AbPWDc