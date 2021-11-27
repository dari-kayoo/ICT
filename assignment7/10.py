#input
number = int(input("Number: "))
ldigit = number%10 # finding las digit
# checking: if no remainder number is divisible
if ldigit%3 == 0:
    print(str(number) + "is dividible by 3")
else:
    print("Indivisible by 3")