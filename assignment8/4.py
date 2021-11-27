# def p(k):
#     t = 2
#     while t*t <= k and k%t != 0:
#         t+=1
#     return (t*t>k)
# input:
s = int(input("Enter starting number: "))
e = int(input("Enter ending number: "))

print("Prime numbers between", s, "and", e, "are:", sep = " ")

for i in range(s, e):# i is numbers between s and e 
    t = 2# prime number starts from 2
    while t*t <= i and i%t != 0: # there is properties of prime num.(Can dividible by 1 and oneself)
        t+=1# then to check divisibility we increase number
    if(t*t>i):# if it is prime we print it.
        print(i)

    # if p(i):
    #     print(i)