"""This prograam will go through with the law of sines with SSA and SAA triangles"""
from math import *
while True:
    option = int(input("Do you want to do the law of sines with SSA(1) or SAA(2) triangles. You can enter 0 to quit.  "
                       ""))

    if option  == 1:
        print("\nAll values must be entered in either decimal or integer form.\n")
        """
        Used to gather all the information needed to solve for the value of the angle opposite of the first side in 
        an SSA triangle, in which two sides' values are known and the value of the angle opposite of the first side
        is known
        """
        A = float(input("Please enter a value for angle A, which is opposite of one of the sides in the triangle.  "))
        a = float(input("Please enter a value for side a which is opposite of angle A.  "))
        b = float(input("Please enter a value for side b which is adjacent to side a.  "))

        A *= pi/180 # Converts angle A into radians
        B = asin(((b*sin(A))/a))

        print(B * 180/pi) # Recoverts the answer from radians to degrees
        """Round to nearest whole number like when answer is 44.99999999999999"""

    elif option == 2:
        print("\nAll values must be entered in either decimal or integer form.\n")
        """
        Used to gather all the information needed to solve for the value of the side opposite of the first angle in 
        an SAA triangle, in which two angles' values are known and the value of the side opposite of the second angle
        is known
        """
        a = float(input("Please enter a value for one side for side a.  "))
        B = float(input("Please enter for an angle value adjacent side a.  "))
        A = float(input("Please enter for an angle opposite side a.  "))
        # Next two lines convert angles from degrees to radians.
        B *= pi/180
        A *= pi/180

        b = (a*sin(B))/sin(A) # Calculates the value of side b opposite of angle B
        print(b)

    elif option == 0: # Will end the program's infinite loop
        break

    else:
        print("\nPlease enter a valid option number\n")
