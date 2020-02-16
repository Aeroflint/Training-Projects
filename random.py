#Задача
'''
Запросите у пользователя четыре числа. Отдельно сложите первые два
и отдельно вторые два. Разделите первую сумму на вторую.
Выведите результат на экран так, чтобы ответ содержал две цифры после запятой.
'''


#Решение

number1 = float(input('Write 1th number: '))
number2 = float(input('Write 2th number: '))
number3 = float(input('Write 3th number: '))
number4 = float(input('Write 4th number: '))

answerOne = number1 + number2
answerTwo = number3 + number4

mainAnswer = answerOne / answerTwo

print("%.2f" % (mainAnswer))