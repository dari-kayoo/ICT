#given:
numbers = [12, 75, 151, 108, 147, 324, 30]
for n in numbers:
    if n > 300: # if num more than 300 we need stop. 
        #If it will be after (divisible by 3) or (greater than 120) will be printed this number
        break
    if n > 120: # condition to check is it greater than 120
        continue
    if n % 3 == 0: # checking divisiblity
        print(n)
    
    
                
        
    
