def p(k):
    t = 2
    while t*t <= k and k%t != 0:
        t+=1
    return (t*t>k)

s = int(input("start = "))
e = int(input("end = "))

print("Prime numbers between", s, "and", e, "are:", sep = " ")

# for i in range(s, e):
#     t = 2
#     while t*t <= i and i%t != 0: 
#         t+=1
#     if(t*t>i):
#         print(i)
for i in range(s, e):
    if p(i):
        print(i)