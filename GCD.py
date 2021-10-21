import math
def gcd(a, b):

    if (a == 0):
        return b
    if (b == 0):
        return a

    if (a == b):
        return a 

    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)









a = 66528
b= 52920

  

print (math.gcd(a, b))