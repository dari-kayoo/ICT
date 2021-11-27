# input
held = int(input())
attended= int(input())
# Finding percentage of attendance:
# From all of class, I found atended class percentage

#total(atten+held) - 100%
#attended - (atten)%
atten = attended*100/(attended+held)
print("Attendance: " + str(round(atten)) + "%")
if atten >= 75:
  print("Welcome! You are allowed to sit in exam")
else:
  print("Sorry. You are NOT allowed to sit in exam")