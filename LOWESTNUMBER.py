def instruction():
    print('FOLLOW THE INSTRUCTION GIVEN BELOW.')
instruction()

def setout_num(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num1 and num2< num3:
        return num2
    elif num3 < num1 and num3 < num2:
        return num3

digit_1 = float(input('Please enter your FIRST NUMBER: '))
digit_2 = float(input('Please enter your SECOND NUMBER:'))
digit_3 = float(input('Please enter your THIRD NUMBER: '))

answer = setout_num(num1 = digit_1, num2 = digit_2, num3 = digit_3)
print(f'The lowest number among the three you have been inputted is {answer:.2f}.')

