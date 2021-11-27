def f(k):
    if k == 0:
        return k
    if k <= 2:
        return 1
    return f(k-1) + f(k-2)
# input:
n = int(input("Enter number of terms: "))
print("Fibonacci sequence: ")
# I create first 2 fib numbers to count the following numbers;
fib1 = 0
fib2 = 1
print(fib1, fib2, sep = " ", end = " ")# then I print first 2 fibnums.
for i in range(n - 2): # this loop count all 10 sum after fib num. so we need minus first sums: fib1, fib2
    fib1, fib2 = fib2, fib1 + fib2 # this is property of fib. num 13+21 = 24 there is following number is sum of first two;
    #output:
    print(fib2, end = " ")
    # print( f(i), end = " ")