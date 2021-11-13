def age():
    age = int(input('Please specify your \033[35m\033[1mage\033[0m\033[0m: '))
    if age >-1 and age <= 12:
        print('\033[1m\033[91m\033[4mKID!\033[0m\033[0m\033[0m')
    elif age >= 13 and age <= 17:
        print('\033[1m\033[91m\033[4mTEEN!\033[0m\033[0m\033[0m')
    elif age == 18:
        print('\033[1m\033[91m\033[4mDEBUT!\033[0m\033[0m\033[0m')
    else:
        print('\033[1m\033[91m\033[4mADULT!\033[0m\033[0m\033[0m')
def display():
    print('\033[1m\033[94m>> DONE!!! <<\033[0m\033[0m')
age()
display()