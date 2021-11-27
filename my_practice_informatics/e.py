v = int(input())
t = int(input())
if v > 0:
    s = v*t
    res = s%109  
    if res == 109:
        res = 0
    print(s%109)
else:
    s = -v*t
    res = 109 - s%109
    if res == 109:
        res = 0
    print(res)

