def age():
    age = int(input('Please enter your age: '))
    if age >-1 and age <= 12:
        print('KID!')
    elif age >= 13 and age <= 17:
        print('TEEN!')
    elif age == 18:
        print('DEBUT!')
    else:
        print('ADULT!')
def display():
    print('>> PROGRAM FINISHED! <<')
age()
display()