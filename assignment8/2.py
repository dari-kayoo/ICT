# def s(k):
#     sum = 0
#     while(k != 0):
#         sum += k
#         k -= 1
#     return sum

# input:
n = int(input("Enter number: "))
# copy data of n;
k = n
sum = 0
while(k != 0): # while copy of n won't be 0 we minus 1. And count sum .
    sum += k
    k -= 1
print("Sum of first", n, "numbers is:", sum, sep = " ")
print("Average of", n, "numbers is:",sum/n, sep = " ")
# print(s(n))
# print(s(n)/n)
