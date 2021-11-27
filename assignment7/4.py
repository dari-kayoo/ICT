#input
salary = int(input("salary: "))
year = int(input("Year of service: "))
# if year of service is more than 5 year, we find bonus. Otherwise output is "No bonus"
if year > 5:
    print ("Bonus is : " + str(salary*0.05))
else:
    print ("No bonus") 