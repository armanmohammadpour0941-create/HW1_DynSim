import math
from component import Component


def calc_henry_cons(component_list: list[Component],composition: list[float], 
                    temprature , a_ij , b_ij, component_index) -> float:
    hery_cons = []
    i = component_index
    Vc = [0.127, 5.71e-2, 0.368, 0, 0.209]
    sum = 0
    sum_len_H = 0
    for j in range(len(component_list)) :
        if i == j :
            continue
        A = a_ij[j][i]
        B = a_ij[i][j]
        C = b_ij[j][i]
        D = b_ij[i][j]
        ln_henry_ij =  A + (B / temprature) + C * math.log(temprature) + D * temprature 
        hery_cons.append(ln_henry_ij)
        sum += composition[j] * Vc[j]**(2/3)
    
    Vc.pop(3)
    x = composition.copy()
    x_new = [x[i] for i in range(len(x))]
    
    x = x_new
    x.pop(3)
    
    for i in range(len(Vc)) :
        sum_len_H += ((x[i] * Vc[i]**(2/3)) / sum) * hery_cons[i]
        
    return math.exp(sum_len_H)      # Kpa

    
    
    