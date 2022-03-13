"""This program will go through with the law of cosines with both SAS and SSS"""
from math import *
while True:
    option = int(input("Do you want to do the law of cosines with SSA(1) or SSS(2). You can type 0 to quit.  "))

    if option == 1:
        print("\nAll values must be entered in decimal or integer form\n")
        """
        Used to gather all the information needed to calculate the side opposite of the angle in an SAS angle where the
        values of two sides adjacent to an angle are known, as well as the angle.
        """
        C = float(input("Please enter a value for angle C, which is the angle opposite of the side you are solving for."
                        "  "))
        b = float(input("Please enter a value for side b, adjacent to angle C  "))
        a = float(input("Please enter a value for side a, adjacent to angle C as well. Switching the value for side b "
                        "and a won't change the value of the final answer.  "))
        # Next line calculates the side length using the information collected
        c = sqrt((a**2)+(b**2)-(2*a*b*cos((C)*(pi/180)))) # The angle C value is converted to radians
        print(c)

    elif option == 2:
        print("\nAll values must be entered in decimal or integer form\n")
        """
        Used to gather all information needed to calculate the angle opposite of a chosen side in a SSS triangle, where
        the length of all sides of a triangle are known and the angle opposite of a chosen side will be solved for
        in this program.
        """
        c = float(input("Please enter the length of the side opposite of the angle that you want to solve for(side c)."
                        "  "))
        b = float(input("Please enter the length of the side adjacent to side c.  "))
        a = float(input("Please enter the length of another side opposite to side c. Switching the value of side b and"
                        " this value(side a) won't change the final answer.  "))
        # The next line calculates the angle to be solved for with the information collected
        C = acos(((c**2)-(a**2)-(b**2))/(-2*a*b))
        print(C * (180/pi)) # Converts the answer from radians to degrees.
        # If the output is something like 60.00000000000001, it is a whole number

    elif option == 0:
        break # Disrupts the infinite loop

    else: # Checks if the number inputted by the user is a valid option
        print("Please enter a valid number for choosing an option.")
