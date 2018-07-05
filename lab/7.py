#Wap to calculate area and circumfrence of a circle
import math
import sys
rad=int(sys.argv[1])
area=math.pi*(rad**2)
circumfrence=2*math.pi*rad
print("Area = {0:.3f}\nCircumfrence = {1:.3f}".format(area,circumfrence),end="")
