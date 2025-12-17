from Antoin_law import calc_p_sat
from unit import kelvin_to_celciuos


class Component :
    def __init__(self, name, pc, tc, acentric_factor, 
                 antoine_coeff: list[float], mw, cp_coeff: list[float], h_vap):
        self.name = name
        self.pc = pc
        self.tc = tc
        self.acentric_factor = acentric_factor
        self.antoine_coeff = antoine_coeff
        self.mw = mw
        self.cp_coeff = cp_coeff
        self.h_vap = h_vap

    def p_sat(self, t) :
        a = self.antoine_coeff[0]
        b = self.antoine_coeff[1]
        c = self.antoine_coeff[2]
        return calc_p_sat(a, b, c, kelvin_to_celciuos(t))
    
        

           
