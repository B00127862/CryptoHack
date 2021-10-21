import math
def egcd(p, q):

    if (p == 0):
        return q, 0, 1

    else:
        (gcd, u, v) = egcd(q%p, p)
        return (gcd, v -(q // p) * u, u)
    
   

p, q = 26513, 32321
gcd, u, v = egcd(p, q) 
print(u, v, )
    

    
