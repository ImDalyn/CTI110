#Dalyn Stiles
#06/19/2024
#P2Lab1
#Moving decimals and calculating circle formulas

#Get radius from the user
import math

radius= float(input("Enter the radius:"))

#Calculate the circumference, diameter, and area.

circumference=2 * math.pi * radius
diameter= 2 * radius
area=math.pi * (radius**2)

#Display the results with decimals

print(f"The diameter of the circle is {diameter:.1f}")
print(f"The circumference of the cirrcle is {circumference:.2f}")
print(f"the area of the circle is {area:.3f}")