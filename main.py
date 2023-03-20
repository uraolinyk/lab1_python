import sys
import math
a = float(input("First number"))
b = float(input("Second number"))
c = float(input("Third number"))
x1 = 0
x2 = 0
delta = 0
if a!= 0:
 delta = b * b - 4 * a * c
else:
 sys.exit("Not correct")
if delta > 0:
 print(delta)
 x1 = (-b + math.sqrt(delta)) / (2 * a)
 x2 = (-b - math.sqrt(delta)) / (2 * a)
 print("Result:", + x1,x2)
if delta == 0:
 print(delta)
 x1 = -b / (2 * a)
 print("Result:", + x1)
else:
 print("No result")