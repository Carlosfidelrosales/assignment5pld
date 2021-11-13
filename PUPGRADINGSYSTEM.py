print('WELCOME TO THE PUP HANDBOOK 2014. SECTION 8. THE PUP GRADING SYSTEM')
print('>>>> FOR OTHER STUDENTS : KINDLY TYPE -1 IF YOU ARE INCOMPLETE, -2 IF YOU ARE WITHDRAWN, -3 IF YOU ARE DROPPED <<<<')
def percentage_revealed():
    your_grade = round(float(input('Please Enter Your Grade to the Space Provided on the Side: ')))
    return your_grade

inserted_grade = percentage_revealed()    

if inserted_grade >= 97 or inserted_grade == 100:
    print(f'Based to your provided Inserted Grade: {inserted_grade}')
    print('Your Grade/Mark is 1.00')
    print('Description is EXCELLENT!')
elif inserted_grade >= 94 or inserted_grade == 96:
    print(f'Based to your provided Inserted Grade: {inserted_grade}')
    print('Your Grade/Mark is 1.25')
    print('Description is EXCELLENT!')
elif inserted_grade >= 91 or inserted_grade == 93:
    print(f'Based to your provided Inserted Grade: {inserted_grade}')
    print('Your Grade/Mark is 1.50')
    print('Description is VERY GOOD!')
elif inserted_grade >= 88 or inserted_grade == 90:
    print(f'Based to your provided Inserted Grade: {inserted_grade}')
    print('Your Grade/Mark is 1.75')
    print('Description is VERY GOOD!')
elif inserted_grade >= 85 or inserted_grade == 87:
    print(f'Based to your provided Inserted Grade: {inserted_grade}')
    print('Your Grade/Mark is 2.0')
    print('Description is GOOD!')
elif inserted_grade >= 82 or inserted_grade == 84:
    print(f'Based to your provided Inserted Grade: {inserted_grade}')
    print('Your Grade/Mark is 2.25')
    print('Description is GOOD!')
elif inserted_grade >= 79 or inserted_grade == 81:
    print(f'Based to your provided Inserted Grade: {inserted_grade}')
    print('Your Grade/Mark is 2.5')
    print('Description is SATISFACTORY!')
elif inserted_grade >= 76 or inserted_grade == 78:
    print(f'Based to your provided Inserted Grade: {inserted_grade}')
    print('Your Grade/Mark is 2.75')
    print('Description is SATISFACTORY!')
elif inserted_grade == 75:
    print(f'Based to your provided Inserted Grade: {inserted_grade}')
    print('Your Grade/Mark is 3.00')
    print('Description is PASSING!')
elif inserted_grade >=65 or inserted_grade == 74: 
    print(f'Based to your provided Inserted Grade: {inserted_grade}')
    print('Your Grade/Mark is 5.00')
    print('Description is FAILURE!')
elif inserted_grade >=0 or inserted_grade ==64:
    print(f'Based to your provided Inserted Grade: {inserted_grade}')
    print('No Grade/Mark can be presented.')
    print('Description is FAILURE!')
elif inserted_grade == -1:
    print(f'Based to your provided Inserted Grade: {inserted_grade}')
    print('No Grade/Mark can be presented.')
    print('Description is INCOMPLETE!')
elif inserted_grade == -2:
    print(f'Based to your provided Inserted Grade: {inserted_grade}')
    print('No Grade/Mark can be presented.')
    print('Description is WITHDRAWN!')
elif inserted_grade == -3:
    print(f'Based to your provided Inserted Grade: {inserted_grade}')
    print('No Grade/Mark can be presented.')
    print('Description is DROPPED!')


#Did'nt use the \n in the print function for each if/elif statement to make me not confused and make it presentable while doing the program.

