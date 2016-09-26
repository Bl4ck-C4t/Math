import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
D = pow(b,2) - (4*(a*c))
x1 = (-b + math.sqrt(D))/(2*a)
x2 = (-b - math.sqrt(D))/(2*a)
print("x1 = {}; x2 = {}".format(x1,x2))
input("Press any key to exit...")
