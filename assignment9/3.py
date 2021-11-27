def repeated(nums):
    d = dict() 
    for i in nums:
        if i in d: 
            print(i)
            break
        else: 
            d[i] = 0

s = input()
new_string = ''
for i in s:
    if i >= '0' and i <= '9' or i == ',':
        news+=i
 
nums = list(map(int, new_string.split(',')))

repeated(nums)