'''
 values - список значений случайной величины
    probabilities - список соответствующих вероятностей
'''

import math


def math_ozhid(values, probabilities):
    result = 0
    for i in range(len(values)):
        result += values[i] * probabilities[i]
    return result


def disper(values, probabilities):

    mu = math_ozhid(values, probabilities)

    second_moment = 0
    for i in range(len(values)):
        second_moment += (values[i] ** 2) * probabilities[i]

    return second_moment - (mu ** 2)


def otklon(values, probabilities):
    var = disper(values, probabilities)
    return math.sqrt(var)


values = list(map(int, input('Введите список значений случайной величины: ').split()))
probabilities = list(map(float, input('Введите список соответствующих вероятностей: ').split()))

print('математичесkое ожидание =', math_ozhid(values, probabilities))
print('дисперсия =', disper(values, probabilities))
print('среднее квадратичного отклонения=', otklon(values, probabilities))