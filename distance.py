import math

# function to calculate distance between two points
def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

# take input from user
x1 = float(input("Enter x-coordinate of point 1: "))
y1 = float(input("Enter y-coordinate of point 1: "))
x2 = float(input("Enter x-coordinate of point 2: "))
y2 = float(input("Enter y-coordinate of point 2: "))

# calculate distance and print result
dist = distance(x1, y1, x2, y2)
print("The distance between the two points is", dist)
