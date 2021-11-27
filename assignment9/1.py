def num_of_good_pairs(nums): 
    d = dict() 
    good_pairs = 0 
    for num in nums: 
        if num in d: 
            good_pairs += d[num]
            d[num] += 1 
        else:
            d[num] = 1 
    return good_pairs 
  
s = input() 
new_string = '' 
for i in s: 
    if i >= '0' and i <= '9' or i == ',': 
        new_string+=i
  
nums = list(map(int, new_string.split(','))) 
print(num_of_good_pairs(nums))

