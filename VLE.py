from component import *
import numpy as np

class LiquidPhase :
    def __init__(self, component_list: list[Component], 
                 pressure: float, temperature: float, a_ij, b_ij):
        
        self.component_list = component_list
        self.number_of_component = len(component_list)
        self.pressure = pressure
        self.temperature = temperature
        self.a = a_ij
        self.b = b_ij
        
  
class VaporPhase :
    def __init__(self, component_list: list[Component], 
                 pressure: float, temperature: float):
        self.component_list = component_list
        self.number_of_component = len(component_list)
        self.pressure = pressure
        self.temperature = temperature
        

class VLESystem :
    def __init__(self, component_list: list[Component], 
                 temperature, pressure, composition: list[float], a_ij, b_ij,
                 inlet_flow) :
        self.component_list = component_list
        self.liquid_phase = LiquidPhase(component_list, pressure, temperature, a_ij, b_ij)
        self.vapor_phase = VaporPhase(component_list, pressure, temperature)
        self.composition = composition
        self.temperature = temperature
        self.pressure = pressure
        self.inlet_flow = inlet_flow
          


        


        
                
        