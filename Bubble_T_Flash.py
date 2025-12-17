

from VLE import VLESystem


class BubbleTFlash :
    def __init__(self, vle_system: VLESystem, vapor_fraction: float, temperature: float) :
        self.vle_system = vle_system
        self.vapor_fraction = vapor_fraction
        self.temperature = temperature