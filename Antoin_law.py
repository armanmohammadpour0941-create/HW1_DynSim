import math
from component import *
def calc_p_sat(component: Component, t) :
    a = component.antoine_coeff[0]
    b = component.antoine_coeff[1]
    c = component.antoine_coeff[2]
    p = math.exp( a - ( b / ( t + c ) ))
    return p             # Pressure (Kpa) , Temperature (C)

def calc_t_sat(component: Component, p) :
    a = component.antoine_coeff[0]
    b = component.antoine_coeff[1]
    c = component.antoine_coeff[2]
    t = ( b / (a - math.log10(p) )) - c
    return t