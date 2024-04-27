
import logging
import random

logging.basicConfig(level=logging.DEBUG, filename='py_log2.log', filemode='w', format='%(asctime)s %(levelname)s %(message)s')

def random_numbers(min_number, max_number):
    if min_number < 0 or max_number < 0:
        logging.warning('Ошибка: границы диапазона не должны быть меньше нуля.')
        print('Недопустимые границы диапазона: числа должны быть ноль или больше!')
        return
    elif min_number >= max_number:
        logging.warning('Ошибка: минимальное значение должно быть меньше максимального.')
        print('Недопустимые границы диапазона: минимальное число должно быть меньше максимального!')
        return
    else:
        return random.randint(min_number, max_number)

while True:
    try:
        input_values = input('Введите минимальное и максимальное число диапазона через пробел: ')
        if not input_values.strip():
            logging.warning('Ошибка: пустой ввод. Требуется ввести два числа.')
            print('Ошибка: пустой ввод. Пожалуйста, введите два числа.')
            continue
        min_number, max_number = map(int, input_values.split())
        random_num = random_numbers(min_number, max_number)
        if random_num is not None:
            print(f'Случайное число в заданном диапазоне: {random_num}')
            break
    except ValueError:
        logging.warning('Ошибка: ввод должен содержать только целые числа.')
        print('Ошибка: ввод должен содержать только целые числа. Попробуйте снова!')

