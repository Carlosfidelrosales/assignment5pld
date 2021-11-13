def instruction():
    print('FOLLOW THE \033[1m\033[95mINSTRUCTIONS\033[0m\033[0m GIVEN BELOW.')
instruction()

def setout_num(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num1 and num2< num3:
        return num2
    elif num3 < num1 and num3 < num2:
        return num3

digit_1 = float(input('\033[1m\033[33mPlease enter your \033[4mFIRST NUMBER\033[0m:\033[0m\033[0m '))
digit_2 = float(input('\033[1m\033[33mPlease enter your \033[4mSECOND NUMBER\033[0m:\033[0m\033[0m '))
digit_3 = float(input('\033[1m\033[33mPlease enter your \033[4mTHIRD NUMBER\033[0m:\033[0m\033[0m '))

answer = setout_num(num1 = digit_1, num2 = digit_2, num3 = digit_3)
print(f'\033[36mThe lowest number among the three you have been inputted is\033[0m \033[4m\033[1m{answer:.2f}\033[0m\033[0m.')

