from component import *
import numpy as np
from NRTL import calc_activity_coeff
from SRK import calc_fugacity_coeff
from K_value import *
from Herny_law import calc_henry_cons
class LiquidPhase :
    def __init__(self, component_list: list[Component], a_ij, b_ij):
        
        self.component_list = component_list
        self.number_of_component = len(component_list)
        self.a = a_ij
        self.b = b_ij
        
    def activity_coeff(self, liquid_composition: list[float], temperature) :
        gamma = calc_activity_coeff(liquid_composition, self.a, self.b, temperature)
        return gamma 
   
  
class VaporPhase :
    def __init__(self, component_list: list[Component]) : 

        self.component_list = component_list
        self.number_of_component = len(component_list)
    
    def fugacity_coeff(self, vapor_composition: list[float], pressure, temperature) :
        phi = calc_fugacity_coeff(self.component_list, vapor_composition,pressure, temperature)
        return phi
    
    
        

class VLESystem :
    def __init__(self, component_list: list[Component], 
                 composition: list[float], a_ij, b_ij,
                 inlet_flow) :
        self.component_list = component_list
        self.liquid_phase = LiquidPhase(component_list, a_ij, b_ij)
        self.vapor_phase = VaporPhase(component_list)
        self.composition = composition
        self.inlet_flow = inlet_flow
        
    def bubble_P(self, temperature) :
        P = 0
        for i in range(len(self.component_list)) :
            component = self.component_list[i]
            if component.name == "CO2" :
                henry_cons = calc_henry_cons(self.component_list, self.composition, 
                                            temperature, self.liquid_phase.a, 
                                            self.liquid_phase.b, i)
                P_i_sat = henry_cons
            else :
                gamma_i = self.liquid_phase.activity_coeff(self.composition, temperature)[i]
                p_i_sat = component.p_sat(temperature)
                P_i_sat = gamma_i * p_i_sat
            P += self.composition[i] * P_i_sat
        return P



    def calculate_k_value(self, liquid_composition: list[float], 
                          vapor_composition: list[float], temperature) :
        k = []
        pressure = self.bubble_P(temperature)
        gamma = self.liquid_phase.activity_coeff(liquid_composition, temperature)
        phi = self.vapor_phase.fugacity_coeff(vapor_composition, pressure, temperature)
        henry_cons = calc_henry_cons(self.component_list, liquid_composition, 
                                    temperature, self.liquid_phase.a, 
                                    self.liquid_phase.b, 3)
        p_sat = []
        for i in range(len(self.component_list)) :
            if i == 3 :
                continue
            component = self.component_list[i]
            p_i_sat = component.p_sat(temperature)
            p_sat.append(p_i_sat)

        for component in self.component_list :
            i = self.component_list.index(component)
            if component.name == "CO2" :
                k_i = k_value_by_henry(henry_cons, phi[i], pressure)
                k.append(k_i)
            else :
                k_i = k_value_by_p_sat(gamma[i], p_sat[i if i<3 else i-1], phi[i], pressure)
                k.append(k_i)
        return k
                

        


        
                
        