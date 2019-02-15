


user_input = input('Введите два числа и математическую операцию в польской нотации: ')
operation_list = ['+', '-','*','/']
num_list =[]

assert user_input[0] in operation_list, 'Ввели неверную операцию'
num_list = user_input.split()

if user_input[0] == '/':
    try:
        print('Итого: {}'.format(int(num_list[1]) / int(num_list[2])))
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    except ValueError:
        print ('Ввели слова вместо чисел!')
    except IndexError:
        print('Ввели пробел вместо числа!')
elif user_input[0] == '*':
    try:
        print('Итого: {}'.format(int(num_list[1]) * int(num_list[2])))
    except ValueError:
        print ('Ввели слова вместо чисел!')
    except IndexError:
        print('Ввели пробел вместо числа!')
elif user_input[0] == '+':
    try:
        print('Итого: {}'.format(int(num_list[1]) + int(num_list[2])))
    except ValueError:
        print ('Ввели слова вместо чисел!')
    except IndexError:
        print('Ввели пробел вместо числа!')
elif user_input[0] == '-':
    try:
        print('Итого: {}'.format(int(num_list[1]) - int(num_list[2])))
    except ValueError:
        print ('Ввели слова вместо чисел!')
    except IndexError:
        print('Ввели пробел вместо числа!')
