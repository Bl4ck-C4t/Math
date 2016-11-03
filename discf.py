import re
from arit import *
def sign(nm):
    nm = str(nm)
    if float(nm) > 0:
        sign = "-"
    else:
        sign = "+"
    if isFloat(float(nm)):
        nm = sign + drb(abs(float(nm)))
    else:
        nm = sign + str(int(float(nm)))
    return nm
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
res = disc(a,b,c)
ch = re.search(r"x1 = ([0-9.\-]+)\nx2 = ([0-9.\-]+)",res)
fg = a
if fg == 1:
    fg = ""
if ch != None:
    gr1 = round(float(ch.group(1))*a,3)
    gr2 = round(float(ch.group(2))*a,3)
    print("{}(x{})*(x{})".format(fg,sign(gr1),sign(gr2)))
    print("({0}x{1})*({0}x{2})".format(fg,sign(gr1),sign(gr2)))
else:
    ch = re.search(r"x = ([0-9.\-]+)",res)
    if ch != None:
        gr1 = round(float(ch.group(1)*a),3)
        print("({}x{})**2".format(fg,sign(gr1)))
    else:
        print(res)
#end
