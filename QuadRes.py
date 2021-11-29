import math

p = 29

int = [14, 6, 11]

flg = (min(x for x in range(p) if pow(x,2,p) in int))

print(flg)
