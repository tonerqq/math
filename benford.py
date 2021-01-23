# BENFORD'S LAW
# @author   tonerqq
# @date     23 Jan 2021

import random

data_set_size = int(raw_input("\n ENTER SIZE OF DESIRED DATA SET : "))
data_spread = [0,0,0,0,0,0,0,0,0]

# generate array of random numbers, and count first digits
for i in range(data_set_size):
    # create random number
    rand_gen_num = str(random.randint(1, 9999))
    # get first digit
    first_dig = int(rand_gen_num[0])
    # count in data_spread array
    data_spread[(first_dig - 1)] += 1


# convert total count to percentage of itself and print
print ""
for x in range(9):
    cur_spread_perc = (data_spread[x] / float(data_set_size)) * 100
    print(" THE NUMBER " + str(x+1) + " OCCURS " + str(cur_spread_perc) + "% OF THE TIME")
