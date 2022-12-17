from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'


def calculate_square_root(your_number):
    """Вычисляет квадратный корень."""
    return sqrt(your_number)


def calc(your_number):
    """Сравнивает."""
    if your_number <= 0:
        return


print(message)
result = calculate_square_root(25.5)
print('Мы вычислили квадратный корень из введённого вами числа.'
      'Это будет:', result)
      