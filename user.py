
#Задача

'''
Напишите программу (файл user.py), которая запрашивала бы у пользователя:
- его имя (например, "What is your name?")
- возраст ("How old are you?")
- место жительства ("Where are you live?")
После этого выводила бы три строки:
"This is имя"
"It is возраст"
"(S)he live in место_жительства"
Вместо имя, возраст, место_жительства должны быть данные, введенные пользователем.
Примечание: можно писать фразы на русском языке, но если вы планируете стать
профессиональным программистом, привыкайте к английскому.
'''


#Решение

userName = input('What is your name?: ')
userOld = input('How old are you?: ')
cityUser = input('Where are you live?: ')

print('This is ' + userName)
print('It is ' + userOld)
print('You live in ' + cityUser)