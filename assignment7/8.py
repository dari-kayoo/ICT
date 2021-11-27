# input:
first = int(input())
second = int(input())
third = int(input())

# There is I compare ages:
if first >= second and first >= third:
    print("Oldest is " + str(first)) # At first I found oldest
    if second >= third: # then Youngest, after finding oldest I have 2 ages to compare. So I have 2 conditions(if/else)
        print("Youngest is " + str(third))
    else:
        print("Youngest is " + str(second))
# There I swap ages and do as first conditions
elif second >= first and second >= third: 
    print("Oldest is " + str(second))
    if first >= third:
        print("Youngest is " + str(third))
    else:
        print("Youngest is " + str(first))
elif third >= first and third >= second:
    print("Oldest is " + str(third))
    if first >= second:
        print("Youngest is " + str(second))
    else:
        print("Youngest is " + str(first))    
else:
    print("They are the same age")
