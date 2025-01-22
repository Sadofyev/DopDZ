# Задание 1
red = input("Сколько красных дней: ")
green = input("Сколько зеленых дней: ")
yellow = input("Сколько желтых дней: ")

total = (int(red)+int(green)+int(yellow))

print("Всего",total,"дней")
print(f"Всего {total} дней")
print("Всего {} дней".format(total))

# Задание 2
salary = input("Зарплата в этом месяце: ")
payment = input("Платеж по кредиту в этом месяце: ")
utility = input("Задолженность за коммунальные услуги: ")

rest = (int(salary)-int(payment)-int(utility))

print("Останется",rest,"после всех выплат.")
print(f"Останется {rest} после всех выплат.")
print("Останется {} после всех выплат.".format(rest))

# Задание 3
diagonal1 = input("Введите диагональ ромба 1 (м): ")
diagonal2 = input("Введите диагональ ромба 2 (м): ")

area = int(diagonal1)*int(diagonal2)/2
# результат area почему-то вещественное число
print("Площадь ромба равна",area,"м2.")
print(f"Площадь ромба равна {area} м2.")
print("Площадь ромба равна {} м2.".format(area))

# Задание 4
print("To be \nor not \nto be")

# Задание 5
print('"Life is what happens \n\twhen \n\t\tyou`re busy making other plans" \n\t\t\t\t\t\t\t\t\tJohn Lennon.')

# Задание 6
meters = input("Введите количество метров: ")

cent = (int(meters)*100)
dec = (int(meters)*10)
mill = (int(meters)*1000)
miles = (int(meters)*0.00062)

print(cent,"сантиметров")
print(dec,"дециметров")
print(mill,"миллиметров")
print(miles,"миль")
# или
print(f"{cent} сантиметров", f"{dec} дециметров", f"{mill} миллиметров",f"{miles} миль",sep="\n")

# Задание 7
number1 = input("Первое число: ")
number2 = input("Второе число: ")

sum = (float(number1)/float(number2))
rounded_sum = round(sum, 2)

print(f"Результат: {rounded_sum}")

# Задание 11
a = 5.0
b = 4.5
a,b = 4.5,5
print(a,b)

# Задание 12
a = 8
b = 1
c = 7
b,a,c = 7,1,8
print(a,b,c)
b,c,a = 8,1,7
print(a,b,c)

# Задание 13
a = 8
p = a*4

r = 3
d = r*2
print("Периметр квадрата:", p, "Диаметр окружности:", d)
print(f"Периметр квадрата: {p} \nДиаметр окружности: {d}")
print("Периметр квадрата: {0} \nДиаметр окружности: {1}".format(p,d))
# Не получается в классическом способе вывести с новой строки. Невозможно т.к. \n работает только для строки?