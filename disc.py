while True:
    import math
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    D = pow(b,2) - (4*(a*c))
    if D < 0:
        print("No sulution D = {}".format(D))
    elif D == 0:
        x = (-b + math.sqrt(D))/(2*a)
        print("x = {}".format(x))
    else:
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
        print("x1 = {}\nx2 = {}".format(x1,x2))
    cb = input("Press 'e' to exit, any key to reset...")
    if cb == "e":
        exit()
