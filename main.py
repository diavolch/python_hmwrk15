# # Возьмите любые 1-3 задания из прошлых домашних заданий. 
# Добавьте к ним логирование ошибок и полезной информации. 
# Также реализуйте возможность запуска из командной строки с 
# передачей параметров.

import logging
import argparse

logging.basicConfig(level=logging.INFO, filename='loger.log', filemode='a', encoding='utf-8',
                    format='%(asctime)s, %(levelname)s, %(message)s')


class SquareException(Exception):

    def __init__(self, message='Такой прямоугольник невозможен!'):
        self.message = message
        super().__init__(self.message)


class NegativeSideException(Exception):

    def __init__(self, message='Стороны не могут быть отрицательными!'):
        self.message = message
        super().__init__(self.message)


class Square:

    def __init__(self, a, b=None):
        if a < 0 or b < 0:
            raise NegativeSideException()
        self._a = a
        if b is None:
            self._b = a
        else:
            self._b = b

    def __add__(self, other):
        if isinstance(other, Square):
            return Square(self._a + other._a, self._b + other._b)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Square):
            if other._a > self._b or other._b > self._b:
                raise SquareException()
            return Square(self._a - other._a, self._b - other._b)
        return NotImplemented

    def get_area(self):
        return self._a * self._b

    def get_perimetr(self):
        return 2*(self._a+self._b)

    def __repr__(self):
        return f"Square({self._a}, {self._b})"

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
        else:
            raise NegativeSideException()

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if value > 0:
            self._b = value
        else:
            raise NegativeSideException()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', type=int, help='Введите сторону a', default=5)
    parser.add_argument('-b', type=int, help='Введите сторону b', default=5)
    args = parser.parse_args()

    try:
        sq = Square(args.a, args.b)
        logging.info(f' Args: {args.a} {args.b}')
    except Exception as e:
        logging.error(e)

