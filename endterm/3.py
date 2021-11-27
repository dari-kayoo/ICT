age = int(input())
sex = input()
marital_status = input()

if sex == 'F':
    print('You will work only in urban areas')
else:
    if age >= 20 and age < 40:
        print('You may work in anywhere')
    elif age >= 40 and age < 60:
        print('You will work in urban areas only') 
    else:
        print('ERROR')
