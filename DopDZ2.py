# 2.8
num = int(input("Введите трехзначное число: "))
digit = num % 10
tens = (num // 10) % 10
hundreds = num // 100
dig_sum = digit + tens + hundreds
dig_mult = digit * tens * hundreds
print(f"Число {num} содержит {digit} единиц, {tens} десятков. \nСумма цифр числа {num} равна {dig_sum}. \nПроизведение цифр числа {num} равно {dig_mult}.")

# 2.9
num = 189
digit = num % 10
tens = (num // 10) % 10
hundreds = num // 100
new_num = digit*100 + tens*10 + hundreds
print(new_num)

# 2.10
num = 982
dig = num % 10
ten = (num // 10) % 10
hund = num // 100
new_num = ten*100 + dig*10 + hund
print(new_num)

# 2.11
num = 128
dig = num % 10
ten = (num // 10) % 10
hund = num // 100
new_num = dig*100 + hund*10 + ten
print(new_num)

# 2.12
num = 128
dig = num % 10
ten = (num // 10) % 10
hund = num // 100
new_num = ten*100 + hund*10 + dig
print(new_num)

# 2.13
num = 891
dig = num % 10
ten = (num // 10) % 10
hund = num // 100
new_num = hund*100 + dig*10 + ten
print(new_num)

# 2.14
num = 873
dig = num % 10
ten = (num // 10) % 10
hund = num // 100
num1 = hund*100 + dig*10 + ten
num2 = ten*100 + hund*10 + dig
num3 = ten*100 +dig*10 + hund
num4 = dig*100 + ten*10 + hund
num5 = dig*100 + hund*10 + ten
print(num, num1, num2, num3, num4, num5)

# 2.15
num = 4831
dig = num % 10
ten = (num // 10) % 10
hund = (num // 100) % 10
thousand = num // 1000
print(thousand+hund+ten+dig)
print(thousand*hund*ten*dig)

# 2.16
num = 8912
dig = num % 10
ten = (num // 10) % 10
hund = (num // 100) % 10
thous = num // 1000
num1 = dig*1000 + ten*100 + hund*10 + thous
num2 = hund*1000 + thous*100 + dig*10 + ten
num3 = thous*1000 + ten*100 + hund*10 + dig
num4 = ten*1000 + dig*100 + thous*10 + hund
print(f"а) {num1}")
print(f"б) {num2}")
print(f"в) {num3}")
print(f"г) {num4}")

# 2.17
n = 84
dig = n % 10
ten = n // 10
print(f"Число {n} содержит {dig} единиц и {ten} десятков.")
print(f"Число {n} содержит {n % 10} единиц и {n // 10} десятков.")

# 2.18
n = 804
ten = (n // 10) % 10
hund = n // 100
print(f"Число {n} содержит {ten} десятков и {hund} сотен.")
print(f"Число {n} содержит {(n // 10) % 10} десятков и {n // 100} сотен.")

# 2.19
n = 4822
hund = (n // 100) % 10
thous = n // 1000
print(f"Число {n} содержит {hund} сотен и {thous} тысяч.")
print(f"Число {n} содержит {(n // 100) % 10} сотен и {n // 1000} тысяч.")
