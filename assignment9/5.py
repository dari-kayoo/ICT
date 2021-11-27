from collections import Counter
def unique_occurence(nums):
    d = {}
    d = Counter(nums)
    if len(d.values()) != len(set(d.values())): 
        return 'false'  
    return 'true' 

s = input()
new_string = ''
for i in s:
    if i >= '0' and i <= '9' or i == ',':
        new_string += i

nums = list(map(int, new_string.split(',')))

print(unique_occurence(nums))