# input:
row = int(input("Enter rows number: "))
i = row
while(i >= 1):# row
    for j in range(1, i + 1):  #  coloumn    
        print(i - j + 1, end = ' ') # printing each value in  decreasing order
    i = i - 1 # decreasing rows while it will be 1. otherwise -> infinite
    print()# new line
