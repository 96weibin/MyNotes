


import logging


def div10(n):
    return 10 / n

def doubleN(n):
    return div10(n) * 2

def main(n):
    return doubleN(n)

try: 
    main(0)
except ZeroDivisionError as e:
    logging.exception('ZeroDivisionError 错误 %s', e)  # ZeroDivisionError 错误 division by zero
except BaseException as e:
    logging.exception('base 错误')
finally:
    print('--------------finally a error logging------------split----------')


print('End')        # try 捕获异常后 继续执行
