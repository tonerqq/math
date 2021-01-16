# FIBONACCI SEQUENCE 
# @author  toner
# @date    15 Jan 2021

index = [0,1]

for i in range(100):
    index.append(index[i] + index[i+1])
    print index[i+2]
