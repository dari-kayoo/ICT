# input
quantity = input("Quantity: ")
# One unit will cost 100, quantity's cost is
cost = quantity*100 
# if Cost of purchased quantity is more than 1000, discount of 10%
if cost > 1000:
    print("Total cost: " + str(cost - cost*0.10))
else:
    print("Total cost: " + str(cost)) # else: no discount