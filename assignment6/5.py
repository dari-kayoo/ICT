def correctWord(n):
    ls = n%100
    if ls == 11 or ls == 12 or ls == 13 or ls == 14:
        return "bochek"

    ls = n%10
    if ls == 0 or ls == 5 or ls == 6 or ls == 7 or ls == 8 or ls == 9:
        return "bochek"
    elif ls == 2 or ls == 3 or ls == 4:
        return "bochki" 
    elif ls == 1:
        return "bochka"
n = int(input())
print(str(n) + " " + correctWord(n))