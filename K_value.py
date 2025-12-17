# calculate K value by P_sat

def k_value_by_p_sat(gamma: float, p_sat: float, phi: float, p: float) :
    k = (gamma * p_sat) / (phi * p)
    return k    

# calculate K value by henry constant
def k_value_by_henry(henry_cons: float, phi: float, p: float) :
    k = henry_cons / (phi * p)
    return k