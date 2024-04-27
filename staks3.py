import logging

logging.basicConfig(level=logging.INFO, filename='py_log3.log', filemode='w', format='%(asctime)s %(levelname)s %(message)s')

def find_average(num):
    sum1 = sum(num)
    arithmetic_average = sum1 / len(num)
    return arithmetic_average

while True:
    try:
        num = input('Введите числа через пробел: ')
        num = list(map(int, num.split()))
        
        arithmetic_average = find_average(num)
        print(f'Среднее арифметическое введенных чисел: {arithmetic_average}')
        logging.info(f'Среднее арифметическое введенных чисел: {arithmetic_average}')
        break
    except ZeroDivisionError:
        print('Пустой ввод!')
        logging.error("ZeroDivisionError", exc_info=True)
        logging.error('Пустой ввод')
    
    except ValueError:
        print('Все элементы списка должны быть числами!')
        logging.critical('Все элементы списка должны быть числами!')
    except KeyboardInterrupt:
        logging.info('Ошибка прерывания с клавиатуры')

