#input
weight = float(input("weight = "))
height = float(input("height = "))
# finding BMI
BMI = round(weight / (height * height))

message = ''
# interpretation depend on BMI 
if BMI < 18.5:
    message += 'are underweight.'
elif BMI >= 18.5 and BMI < 25:
    message += 'have a normal weight.'
elif BMI >= 25 and BMI < 30:
    message += 'are slightly overweight.' 
elif BMI >= 30 and BMI < 35:
    message += 'are obese.' 
elif BMI >= 35:
    message += 'are clinically obese.'

print("Your BMI is " + str(BMI) + ", you are " + message)