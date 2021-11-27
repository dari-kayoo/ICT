a = int(input())
b = int(input())
n = int(input())
d = a*n
c = b*n
if(c >= 100):
    d+=c//100
    c = c%100 
print(d, c)
