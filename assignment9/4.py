from collections import Counter
def sum_of_u(nums): 
    d = {}
    sum = 0
    d = Counter(nums) 
    for i in d.keys(): 
        if d[i] == 1: 
            sum += i 
    return sum

s = input()
new_string = ''
for i in s:
    if i >= '0' and i <= '9' or i == ',':
        new_string += i

nums = list(map(int, new_string.split(',')))

print(sum_of_u(nums))
