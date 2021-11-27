h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

h = h2 - h1
m = m2 - m1
s = s2 - s1
res = s + m*60 + h*60*60
print(res)
