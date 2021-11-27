bill = 0
# input:
size = input('size = ')
add_pepperoni = input('add_pepperoni = ')
extra_cheese = input('extra_cheese = ')
# we have 3 kind of size. Each of them we need if statement to add bill
if size == '"S"':
	bill += 15
	if add_pepperoni == '"Y"': # Also for ach pizza we can add pepperoni so it wull be nested for each size
		bill += 2
elif size == '"M"':
	bill += 20
	if add_pepperoni == '"Y"': 
		bill += 3
elif size == '"L"':
	bill += 25
	if add_pepperoni == '"Y"':
		bill += 3
if extra_cheese == '"Y"': # Cheese can be added for any size and cost is one, so we write like not nested 
	bill += 1

# We cannot write add_peporoni like extra_cheese, because differnt cost for Small pizza
print("Your final bill is: $" + str(bill))
