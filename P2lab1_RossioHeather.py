# Heather Rossio
# 02/17/2025
# P2Lab1
# Lab 1 Python Module 4

import math
#Get radius from user as float
radius = float(input("What is the radius of the circle?"))

#Calculate diameter
diameter = 2 * radius

#Calculate circumference
circum = 2 * math.pi * radius

#Calculate area
area = math.pi * radius ** 2

#display values to the user
print(f"The diameter of the circle is {diameter:.1f}")
print()
print(f"The circumference of the circle is {circum:.2f}")
print()
print(f"The area of the circle is {area:.3f}")
