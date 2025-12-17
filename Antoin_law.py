import math
from component import *
def calc_p_sat(a , b, c, t) :
    p = math.exp( a - ( b / ( t + c ) ))
    return p             # Pressure (Kpa) , Temperature (C)

def calc_t_sat(a, b, c, p) :
    t = ( b / (a - math.log10(p) )) - c
    return t