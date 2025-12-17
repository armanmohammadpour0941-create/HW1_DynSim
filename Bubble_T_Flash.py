

from VLE import VLESystem


class BubbleTFlash :
    def __init__(self, vle_system: VLESystem, vapor_fraction: float, temperature: float) :
        self.vle_system = vle_system
        self.vapor_fraction = vapor_fraction
        self.temperature = temperature
        
    def flash_calculation(self, x0: list[float], y0: list[float]) :
        
        liq_composition = x0
        vap_composition = y0
        pressure = self.vle_system.bubble_P(self.temperature)
        k = self.vle_system.calculate_k_value(liq_composition, vap_composition, self.temperature)
        y = [(self.vle_system.composition[i] * k[i]) /(1 + self.vapor_fraction*(k[i] - 1)) for i in range(len(k))]
        x = [y[i] / k[i] for i in range(len(k))]
        
        print(f" pressur : {pressure} \n y : {y} \n x : {x} \n k : {k}")
        
        
        
        