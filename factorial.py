# FACTORIAL OF 100 CALCULATOR
# @author   tonerqq
# @date     16 Jan 2021

# note: this is hardly a challenge considering python can easily store the factorial

fac = 1

for i in range(101):
    if (int(i) != 0):
        fac += fac * i

print fac
print ("length: " + str(len(str(fac))))
