# input
year = int(input())
# As given in the problem: divisible by 4, but not divisible by 100 
# + divisible by 400
if year%4 == 0 and year%100 !=0 or year%400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")
    