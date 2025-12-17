

from VLE import VLESystem
import numpy as np
from scipy.optimize import fsolve
class BubbleTFlash :
    def __init__(self, vle_system: VLESystem, vapor_fraction: float, temperature: float) :
        self.vle_system = vle_system
        self.vapor_fraction = vapor_fraction
        self.temperature = temperature
        
    

    def flash_calculation(self) :

        x0 = [0.2 for i in range(len(self.vle_system.composition))]
        pressure = self.vle_system.bubble_P(self.temperature)
        x = [0 for i in range(len(x0))]
        e = [1 for i in range(len(x))]
        tol = 1e-15
        error = 1
        while error > tol :
            x = x0    
            k = self.vle_system.calculate_k_value(self.vle_system.composition, self.temperature)
            y = [(self.vle_system.composition[i] * k[i]) /(1 + self.vapor_fraction*(k[i] - 1)) for i in range(len(k))]
            x_new = [y[i] / k[i] for i in range(len(k))]
            x0 = x_new
            e = [x[i] - x0[i] for i in range(len(x))]
            error = np.linalg.norm(e)
        
        print(f" pressur : {pressure} \n y : {y} \n x : {x} \n k : {k}")
        
        
        
        