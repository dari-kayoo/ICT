def less_than(nums):  
    a = list(sorted(nums)) 
    return [a.index(i) for i in nums] 

s = input()
new_string = ''
for i in s:
    if i >= '0' and i <= '9' or i == ',':
        news+=i
 
nums = list(map(int, new_string.split(',')))

print(less_than(nums))


