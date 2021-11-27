n = int(input())
k = int(input())
res = n - k%n
if res == n:
    res = 0
print(res)