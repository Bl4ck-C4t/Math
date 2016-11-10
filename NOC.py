import math
import re
from arit import *
def differ(ls,ls2):
    ls3 = []
    ls2 = list(tuple(ls2))
    for x in ls:
        if x in ls2:
            ls2.remove(x)
        ls3.append(x)
    return ls3 + ls2
def diff2(ls):
    while len(ls) != 1:
        c = differ(ls[0],ls[1])
        del ls[0]
        del ls[0]
        ls.insert(0,1)
        ls[0] = c
    return ls[0]
def dividers(ls):
    divs = []
    for num in ls:
        curr = []
        while num != 1:
            for x in range(2,num+1):
                if num % x == 0:
                    curr.append(x)
                    num = int(num/x)
                    break
        divs.append(curr)
    return divs
                
def NOC_num(ls):
    multi = 1
    c = diff2(dividers(ls))
    for x in c:
        multi *= x
    return multi
denoms = []
nums = []
other = []
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
num = 1
if len(nums) > 0:
    num = NOC_num(nums)
other = list(set(other))
other2 = []
for x in other:
    match = re.search("[+\-]",x)
    if match != None:
        match = "({})".format(x)
    else:
        match = x
    other2.append(match)
other = other2
if num != 1:
    other.insert(0,str(num))
denoms = "".join(other)
print(denoms)
