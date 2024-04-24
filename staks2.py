'''Написать программу для генерации случайных чисел в заданном диапазоне.
Если пользователь ввел недопустимые границы диапазона (например, меньше нуля),
программа должна вывести ошибку и попросить ввести диапазон заново.
Информация об ошибках должна быть записана в лог.'''
import logging
import random

logging.basicConfig(level=logging.DEBUG, filename='py_log.log',filemode='w', format='%(asctime)s %(levelname)s %(message)s')
def random_numbers(min_number, max_number):
    if min_number >= 0 and max_number >= 0:
        logging.warning('минимальное число и максимальное должно быть больше 0')
        return random.randint(min_number, max_number)
    else:
        print('Недопустимые границы диапазона!')
        logging.warning('Недопустимые границы диапазона!')
        return

while True:
    try:
        print('Введите минимальное и максимальное число диапазона от 0 и больше через пробел!')
        min_number, max_number = map(int, input().split())
        random_num = random_numbers(min_number, max_number)

        if random_num is not None:
            print(f'Случайное число в заданном диапазоне: {random_num}')
            break

    except ValueError:
        logging.warning('Ошибка: введенные значения должны быть целыми числами от меньшего к большему.')
        print('Ошибка: введенные значения должны быть целыми числами от меньшего к большему.')

