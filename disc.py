import math
from arit import *
while True:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    D = pow(b,2) - (4*(a*c))
    if D < 0:
        print("No sulution D = {}".format(D))
    elif D == 0:
        x = (-b + math.sqrt(D))/(2*a)
        print("x = {}".format(x))
    else:
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
        if isFloat(x1):
            x1 = drb(x1)
        if isFloat(x2):
            x2 = drb(x2)
        print("x1 = {}\nx2 = {}".format(x1,x2))
    cb = input("Press 'e' to exit, any key to reset...")
    if cb == "e":
        exit()
