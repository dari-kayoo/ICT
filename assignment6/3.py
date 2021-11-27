a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == 0 and b == 0: 
    print("INF")
elif a == 0: 
    print("NO")
else:
    x = -b/a
    s = str(x) 
    if s[-2:] != ".0":
       print("NO") 
    else:
        if c*b != a*d: 
            print(int(x))
        else:
            print("NO")
