# Uppgift "8" : Thomas Lindholm

def print_max(number1, number2, number3):
    if number1 >= number2 and number1 >= number3:
        max = number1
    elif number2 >= number1 and number2 >= number3:
        max = number2
    else:
        max = number3
    print (f'Det största talet är {max}')

user_input_number1 = int(input('Skriv in tal 1:'))
user_input_number2 = int(input('Skriv in tal 2:'))
user_input_number3 = int(input('Skriv in tal 3:'))

print_max(user_input_number1,user_input_number2,user_input_number3)

