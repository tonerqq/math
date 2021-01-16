# BINARY TO DECIMAL CONVERTER
# @author   tonerqq
# @date     16 Jan 2021

import sys

bin = input("enter base 2 number for conversion to decimal: ")
dec = 0
exp = len(str(bin)) - 1 

for i in str(bin):
    i = int(i)
    if (i != 0 and i != 1):
        print "ERROR: non-binary number entered! exiting..."
        sys.exit()
    else:
        dec += (i * (2 ** exp))
        exp -= 1

print ("decimal number: " + str(dec))
