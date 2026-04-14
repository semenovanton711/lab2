#номер 1
#import random
#numbers1 = [random.randint(1, 10) for i in range(5)]
#numbers2 = [random.randint(10, 30) for i in range(10)]
#all_numbers = numbers1 + numbers2
#print("5 чисел от 1 до 10:", numbers1)
#print("10 чисел от 10 до 30:", numbers2)
#print("Все 15 чисел:", all_numbers)



#номер 2
#num1 = input("Введите первое число: ")
#num2 = input("Введите второе число: ")
#common_digits = set(num1) & set(num2)
#if common_digits:
#    print("Общие цифры:", ', '.join(sorted(common_digits)))
#else:
#    print("Общих цифр нет")



#номер 4
#result = []
#for num in range(1, 51):
#    if (num % 3 == 0 or num % 4 == 0) and not (num % 3 == 0 and num % 4 == 0):
#        result.append(num)

#print("Числа от 1 до 50:")
#print("Делятся на 3 или на 4, но не на оба одновременно:")
#print(result)



#номер 5
result = set()

for i in range(1, 20, 2):  # шаг 2, чтобы брать только нечетные числа
    if i + 2 <= 20:  # проверяем, чтобы следующее число тоже было в разумных пределах
        result.add((i, i + 2))

print("Множество кортежей с нечетными числами:")
print(result)