# task_1
print('\ntask_1')
P = 1
for k in range(-3, 7):
    P *= abs(k - 7) / 5
print(f'P = {P}')

# task_2
print('\ntask_2')
q = 0
a = float(input('Введіть початок проміжку: '))
b = float(input('Введіть кінець проміжку: '))
print('Введіть 9 дійсних чисел:')
for n in range(9):
    x = float(input())
    if a <= x <= b:
        q += 1
print(f'Кількість чисел, що належать проміжку [{a}; {b}]  = {q}')

# task_3
print('\ntask_3')
n = int(input('Скільки цілих чисел ви хочете ввести: '))
print(f'Введіть {n} цілих чисел:')
for q in range(n):
    x = int(input())
    if (x ** 2) > 10:
        print(f'Квадрат з {x} більший 10')
    else:
        print(f'Квадрат з {x} менший або рівний 10')

# task_4
print('\ntask_4')
s = 0
x = int(input("Введіть шестицифрове натуральне число: "))
if x > 0:
    for i in range(6):
        if x % 10 == 7:
            s += 1
        x = x // 10
print(f'Кількість цифр 7 в числі = {s}')
