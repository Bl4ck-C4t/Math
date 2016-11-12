import math
def disc(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    D = pow(b,2) - (4*(a*c))
    if D < 0:
        return "No solution D = {}".format(D)
    elif D == 0:
        x = (-b + math.sqrt(D))/(2*a)
        return "x = {}".format(x)
    else:
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
        return "x1 = {}\nx2 = {}".format(x1,x2)  
def div(n1,n2):
    def divs(n1,n2):
        n = min(n1,n2)
        for x in range(n,1,-1):
            if n1 % x == 0 and n2 % x == 0:
                return x
        return False
    dv = 1
    while dv != False:
        dv = divs(n1,n2)
        if dv != False:
            n1,n2 = int(n1/dv),int(n2/dv)
        if n2 == 1:
            return str(n1)
    return "{}/{}".format(n1,n2)
def isFloat(num):
    if num > 0:
        return num > int(num)
    return not(num > int(num))
def isInt(check):
    try:
        check = int(check)
        return True
    except:
        return False
def drb(nm):
    c = len(str(nm)[str(nm).index("."):])-1
    nm = int(nm*pow(10,c))
    sign = ""
    if nm < 0:
        sign = "-"
    dv = div(abs(nm),pow(10,c))
    return sign + dv
