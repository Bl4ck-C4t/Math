import math
from arit import *
def NOC(ls):
    
denoms = []
nums = []
other = []
multi = 1
while True:
    znm = input("Enter denominator('s' to stop): ")
    if znm == "s":
        break
    denoms.append(znm)
for x in denoms:
    if isInt(x):
        nums.append(int(x))
    else:
        other.append(x)


if multi != 1:
    denoms.insert(0,str(multi))
denoms = "".join(denoms)
print(denoms)
