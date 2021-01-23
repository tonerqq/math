# AREA CALCULATOR
# @author   tonerqq
# @date     16 Jan 2021

# rectangle & square
# various triangles
# circle 

# print shape choices ASCII
print ""
print(" AREA CALCULATOR : SELECT SHAPE NUMBER")
print("               .   +-----+        x  x")
print("   /\    |    /| | |     | |    x      x")
print("  /  \   |   / | | |     | |   x        x")
print(" /    \  |  /  | | |     | |   x        x")
print("/______\ | /___| | +-----+ |    x      x")
print("                                  x  x")
print("   #1       #2       #3            #4")

# take user input and call handler
user_shape = input(" ENTER NUMBER : ")

# isosceles triangle module ( A = (b*h) / 2 )
def isosceles_triangle(base, height, area):
    if (str(base) == null):
        # 
    elif (str(height) == null):
        #
    elif (str(area) == null):
        # main juice
    else:
        print(" ERROR : invalid input! exiting...")
        sys.exit()

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
	base = input("\n ENTER B : ")
	height = input(" ENTER h : ")
	area = input(" ENTER area : ")
	isosceles_triangle(base, height, area)
    elif (choice == "2"):
        ra_triangle()
    elif (choice == "3"):
        rectangle()
    elif (choice == "4"):
        circle()
    else: 
        print(" ERROR : invalid input! Please select a number.")
        sys.exit()


shape_choice(user_shape)
