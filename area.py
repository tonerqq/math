# AREA CALCULATOR
# @author   tonerqq
# @date     16 Jan 2021

# rectangle & square
# various triangles
# circle 

# import math lib & sys
import math
import sys

# print shape choices ASCII
print ""
print(" AREA CALCULATOR : SELECT SHAPE NUMBER")
print("               .   +-----+      x  x")
print("   /\    |    /| | |     | |  x      x")
print("  /  \   |   / | | |     | | x        x")
print(" /    \  |  /  | | |     | | x        x")
print("/______\ | /___| | +-----+ |  x      x")
print("                                x  x")
print("   #1       #2       #3          #4")

# take user input and call handler
user_shape = input(" ENTER NUMBER : ")

# isosceles triangle module ( A = (b*h) / 2 )
def isosceles_triangle(base, height, area):
    ans = "ERROR"
    if (str(base) == "null"):
        ans = ((2 * int(area)) / int(height))
    elif (str(height) == "null"):
        ans = ((2 * int(area)) / int(base))
    elif (str(area) == "null"):
        ans = ((int(base) * int(height)) / 2)
    else:
        print(" ERROR : invalid input! exiting...")
        sys.exit()
    print("\n ANSWER IS : " + str(ans))

# right angle triangle module 
def ra_triangle(a, b, c):
    ans = "ERROR"
    if (str(a) == "null"):
        a_len = math.sqrt(int(c) ** 2 - int(b) ** 2)
        ans = ((a_len * int(b)) / 2)
    elif (str(b) == "null"):
        b_len = math.sqrt(int(c) ** 2 - int(a) ** 2)
        ans = ((b_len * int(a)) / 2)
    elif (str(c) == "null"):
        ans = ((int(a) * int(b)) / 2)
    else:
        print(" ERROR : invalid input! exiting...")
        sys.exit()
    print("\n ANSWER IS : " + str(ans))

# square / rectangle module
def rectangle(a, b):
    ans = "ERROR"
    if (str(a) == "null" or str(b) == "null"):
        print(" ERROR : both values required for this module! exiting...")
        sys.exit()
    else:
        ans = int(a) * int(b)
    print("\n ANSWER IS : " + str(ans))

# circle module
def circle(r):
    ans = (math.pi * (int(r) ** 2))
    print("\n ANSWER IS : " + str(ans))

# initial shape selection handler
def shape_choice(choice):
    choice = str(choice) 
    if (choice == "1"):
        # get triangle variables
	print("\n ENTER KNOWN VARIABLES, IF UNKNOWN ENTER 'NULL' \n")
	print("      + ")
	print("     /|\ ")
	print("    / | \ ") 
	print("   /  |  \ ")
	print("  /   |h  \ ")
	print(" /    |    \ ")
	print("/_____|_____\ ") 
	print("      B ")
	base = raw_input("\n ENTER B : ")
	height = raw_input(" ENTER h : ")
	area = raw_input(" ENTER area : ")
	isosceles_triangle(base, height, area)
    elif (choice == "2"):
        print("\n ENTER KNOWN VARIABLES, IF UNKNOWN ENTER 'NULL' \n")
        print("  +       ") 
        print("  |\      ")  
        print("  | \     ") 
        print("  |  \    ") 
        print(" A|   \C  ")    
        print("  |    \  ")    
        print("  |     \ ")  
        print("  +------+")
        print("      B   ")
        a_len = raw_input("\n ENTER A : ")
        b_len = raw_input(" ENTER B : ")
        c_len = raw_input(" ENTER C : ")
        ra_triangle(a_len, b_len, c_len)
    elif (choice  == "3"):
        # get sqr / rec variables
        print("\n ENTER KNOWN VARIABLES, IF UNKOWN ENTER 'NULL' \n")
        print("  +-------+ ")
        print("  |       | ")   
        print(" A|       | ")     
        print("  |       | ")    
        print("  +-------+ ")            
        print("      B     ")      
        a_len = raw_input("\n ENTER A : ")
        b_len = raw_input(" ENTER B : ")
        rectangle(a_len, b_len)
    elif (choice == "4"):
        print("\n ENTER RADIUS OF CIRCLE")
        print("    x  x")
        print("  x      x")
        print(" x      r x")
        print("x     -----x (r = radius)")
        print(" x        x")
        print("  x      x")
        print("    x  x")
        radius = raw_input(" ENTER r : ")
        circle(radius)
    else: 
        print(" ERROR : invalid input! Please select a number.")
        sys.exit()


shape_choice(user_shape)
