n = int(input())
s = input()
symbols = ['!','@','#','$','%', '^','&','*', '1', '2', '3', '4','5', '6', '7', '8', '9', '0']

for sy in symbols:
    for i in range(n):
        if sy in s[i]:
            s = s.replace(s[i], '')
print(s)
        

