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

    def set_name(self, name) :
        self.name = name
    def set_pc(self, pc) :
        self.pc = pc
    def set_tc(self, tc) :
        self.tc = tc
    def set_acentric_factor(self, acentric_factor) :
        self.acentric_factor = acentric_factor
    def set_antoine_coeff(self, a, b, c) :
        self.antoine_coeff[0] = a
        self.antoine_coeff[1] = b
        self.antoine_coeff[2] = c
    def set_tc(self, mw) :
        self.mw = mw
    def set_cp_coeff(self, cp_coeff: list[float]) :
        self.cp_coeff = cp_coeff
    def set_h_vap(self, h_vap) :
        self.h_vap = h_vap
    

    def get_name(self) :
        self.name

    def get_pc(self) :
        self.pc
        
    def get_tc(self) :
        self.tc

    def get_acentric_factor(self) :
        self.acentric_factor

    def get_antoine_coeff(self) :
        self.antoine_coeff
    
    def get_mw(self) :
        self.mw 

    def get_cp_coeff(self) :
        self.cp_coeff
        
    def get_h_vap(self) :
        self.h_vap
    
    

           
