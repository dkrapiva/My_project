import random

random_num = random.randint(1, 100)

while True:
    try:
        print('Введите число от 1 до 100: ')
        n = int(input())
    except ValueError:
        print('Необходимо ввести целое число от 1 до 100')
        print()
        continue
    if n < 1 or n > 100:
        print('Число должно быть в диапазоне [1, 100]')
    elif n == random_num:
        print("Вы угадали!")
        print('Test')
        break
    else:
        print('Неверно, попробуйте снова')
        print()