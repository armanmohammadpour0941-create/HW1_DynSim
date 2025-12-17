import math
from unit import *
from component import Component
def solve_cubic_srk(A, B):
    """
    Solves the SRK Cubic Equation: Z^3 - Z^2 + (A - B - B^2)Z - AB = 0
    Returns the real roots (typically up to 3).
    """
    
    # Coefficients of the cubic polynomial: c3*Z^3 + c2*Z^2 + c1*Z + c0 = 0
    c3 = 1.0
    c2 = -1.0
    c1 = A - B - B**2
    c0 = -A * B

    Z = 1.0 
    for _ in range(100): 
        f_z = c3*Z**3 + c2*Z**2 + c1*Z + c0
        f_prime_z = 3*c3*Z**2 + 2*c2*Z + c1
        
        if abs(f_prime_z) < 1e-9: # Avoid division by zero
            break
        
        Z_new = Z - f_z / f_prime_z
        
        if abs(Z_new - Z) < 1e-6:
            break
        Z = Z_new
        
    return Z # Return the best estimate for Z_Vapor

def calc_fugacity_coeff(component_list: list[Component], composition: list[float],  
                        pressure, temperature):
    phi = []
    R = 83.14472  # cm3·bar/(K·mol)
    # SRK Constants
    Omega = 0.08664 # b*Pc / (R*Tc)
    Psi = 0.42748   # a*Pc / (R^2*Tc^2)
    B_is = []
    A_is = []
    B = 0
    A = 0
    Betta = 0
    qbetta = 0
    A_ij = [ [0 for j in range(len(component_list))] for i in range(len(component_list))]
    for component in component_list :
        Tr = temperature / component.tc
        Pr = kpa_to_bar(pressure) / component.pc       
        w = component.acentric_factor
        m = 0.48 + 1.574 * w - 0.176 * w**2
        alpha = (1 + m * (1 - math.sqrt(Tr)))**2
        
        A_i = Psi * alpha * R**2 * component.tc**2 / component.pc
        A_is.append(A_i)
        
        B_i = Omega * R * component.tc / component.pc 
        B_is.append(B_i)
        i = component_list.index(component)
        betta_i = Omega * Tr / Pr
        B += composition[i] * B_i
        Betta += composition[i] * betta_i
        
        q = Psi * alpha / (Omega * Tr)
        qbetta += composition[i] * q*betta_i
        
        sum = 0
        for j in range(len(component_list)) :
            component_j = component_list[j]
            Tr_j = temperature / component_j.tc
            w_j = component_j.acentric_factor
            m_j = 0.48 + 1.574 * w_j - 0.176 * w_j**2
            alpha_j = (1 + m_j * (1 - math.sqrt(Tr_j)))**2
            A_j = Psi * alpha_j * R**2 * component_j.tc**2 / component_j.pc
            A_ij[i][j] = math.sqrt(A_i * A_j)
            sum += composition[i]*composition[j]*A_ij[i][j]
        
        A += sum
    
    Z_V = solve_cubic_srk(qbetta, Betta)

    for i in range(len(component_list)) :
        A_i = A_is[i]
        B_i = B_is[i]
        
        Tr = temperature / component_list[i].tc
        w = component_list[i].acentric_factor
        Pr = kpa_to_bar(pressure) / component_list[i].pc
        m = 0.48 + 1.574 * w - 0.176 * w**2
        alpha = (1 + m * (1 - math.sqrt(Tr)))**2
        
        betta = Omega * Pr / Tr
        q = Psi * alpha / (Omega * Tr)
        I = math.log((Z_V + betta) / Z_V)
        
        q_bar = q * (1 + (A_i / A) - (B_i / B))
        
        ln_phi_i = ((B_i / B) * (Z_V - 1)) - math.log(abs(Z_V - betta)) - q_bar * I
        phi_i = math.exp(ln_phi_i)
        phi.append(phi_i)
    return phi

