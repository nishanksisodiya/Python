#Wap to calculate area and circumfrence of a circle
import math
rad=int(input("Enter Radius : "))
area=math.pi*(rad**2)
circumfrence=2*math.pi*rad
print("Area = {0:.3f}\nCircumfrence = {1:.3f}".format(area,circumfrence),end="")
