print('WELCOME TO THE \033[1m\033[35mPUP HANDBOOK 2014\033[0m\033[0m. SECTION 8. THE PUP GRADING SYSTEM')
print('\033[36m>>>> FOR OTHER STUDENTS : KINDLY TYPE \033[4mINC\033[0m \033[36mIF YOU ARE\033[0m \033[36m\033[1mINCOMPLETE\033[0m, \033[36m\033[4mW\033[0m \033[36m\033[36mIF YOU ARE \033[1mWITHDRAWN\033[0m, \033[36m\033[4mD\033[0m\033[0m \033[36mIF YOU ARE \033[1mDROPPED\033[0m \033[36m<<<<\033[0m\033[0m\033[0m')
def percentage_revealed():
    put_grade = (input('Please \033[4mEnter Your Grade\033[0m to the Space Provided on the Side: '))
    if put_grade.upper == 'INC':
        print(f'Description is \033[92mIncomplete\033[0m')
    elif put_grade.upper == 'W':
        print(f'Description is \033[92mWithdrawn\033[0m')
    elif put_grade.upper == 'D':
        print(f'Description is \033[92mDropped\033[0m')
    else:
        your_grade = round(float(put_grade))
        if your_grade >= 97 and your_grade <= 100:
            print('Your Grade/Mark is \033[92m1.00 \nDescription is \033[92mEXCELLENT\033[0m!')
        elif your_grade >= 94 and your_grade <= 96:
            print('Your Grade/Mark is \033[92m1.25 \nDescription is \033[92mEXCELLENT\033[0m!')
        elif your_grade >= 91 and your_grade <= 93:
            print('Your Grade/Mark is \033[92m1.50 \nDescription is \033[92mVERY GOOD\033[0m!')
        elif your_grade >= 88 and your_grade <= 90:
            print('Your Grade/Mark is \033[92m1.75 \nDescription is \033[92mVERY GOOD\033[0m!')
        elif your_grade >= 85 and your_grade <= 87:
            print('Your Grade/Mark is \033[92m2.0 \nDescription is \033[92mGOOD\033[0m!')
        elif your_grade >= 82 and your_grade <= 84:
            print('Your Grade/Mark is \033[92m2.25 \nDescription is \033[92mGOOD\033[0m!')
        elif your_grade >= 79 and your_grade <= 81:
            print('Your Grade/Mark is \033[92m2.5 \nDescription is \033[92mSATISFACTORY\033[0m!')
        elif your_grade >= 76 and your_grade <= 78:
            print('Your Grade/Mark is \033[92m2.75 \n Description is \033[92mSATISFACTORY\033[0m!')
        elif your_grade == 75:
            print('Your Grade/Mark is \033[92m3.0 \nDescription is \033[92mPASSING\033[0m!')
        elif your_grade >=65 and your_grade <= 74: 
            print('Your Grade/Mark is \033[92m5.0 \nDescription is \033[92mFAILURE\033[0m!')
        else:
            print('Please enter a grade between \033[92m65 to 100\033[0m.')
        return
percentage_revealed()




