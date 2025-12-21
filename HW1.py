from component import Component
from VLE import *
from Bubble_T_Flash import BubbleTFlash
import numpy as np
from scipy.optimize import fsolve
from fsolve import equations

methanole = Component("methanole", 8.22, 513.4, 0.564, 
                      [16.5785, 3638.27, 239.5], 32.04, 
                      [0.0072, 0.3949, 0], 1165)

water = Component("water", 22.12, 647.3, 0.345, 
                  [16.3872, 3885.7, 230.17], 18.01528, 
                  [0.00002, 0.0104, 0], 2399.905)

n_hexane = Component("n-hexane", 3.01, 507.5, 0.301, 
                     [13.8193, 2696.04, 224.317], 86.178, 
                     [0, 0, 2.23], 359.73)

co2 = Component("CO2", 7.38, 304.1, 0.224, 
                [6.81228, 1301.679, -3.494], 44.01, 
                [0.001, 0.5487, 0], 179.5)

acetone = Component("Acetone", 4.69, 508.1, 0.307, 
                    [14.3145, 2756.22, 228.06], 58.08, 
                    [0, 0, 2.14], 534)

component_list = [methanole, water, n_hexane, co2, acetone]

# overall feed composition (mole fractions)
z = [0.25, 0.15, 0.2, 0.25, 0.15]

temperature = 310 # inital guess

inlet_flow = 10 #kmol/h

# NRTL parameters (from earlier file)
# a_ij = [[0, 610.403, 1915.077, 69.676, 118.08],
#      [-48.673, 0, 3908.122, -183.691, 750.318],
#      [1287.78, 5042.121, 0, 69.676, 681.48],
#      [-3094.809, 676.278, -3989.918, 0, -3912.19],
#      [296.243, 1299.305, 476.887, 69.676, 0]]

# b_ij = [[0, 0, 0, -8.408, 0],
#      [0, 0, 0, 39.068, 0],
#      [0, 0, 0, -8.408, 0],
#      [0.001, -0.098, 0.001, 0, 0.001],
#      [0, 0, 0, -8.408, 0]]
a_ij = [[0, 740.34, 1173.36, 69.676, 213.754],
     [-233.016, 0, 3908.122, 69.676, 562.853],
     [1095.042, 5042.121, 0, 69.676, 549.27],
     [-3094.809, -2941.997, -3989.918, 0, -3912.19],
     [206.171, 1017.431, 671.979, 69.676, 0]]

b_ij = [[0, 0, 0, -8.408, 0],
     [0, 0, 0, -8.408, 0],
     [0, 0, 0, -8.408, 0],
     [0.001, 0.001, 0.001, 0, 0.001],
     [0, 0, 0, -8.408, 0]]


max_iter = 100
tol = 0.0002

vapor_fraction = 0.0

x0 = [0.27, 0.16, 0.22, 0.17, 0.18]
y0 = [0.0086, 0.0007, 0.04, 0.927, 0.0237]
vle = VLESystem(component_list, z, a_ij, b_ij, inlet_flow)
flash_calculator = BubbleTFlash(vle, vapor_fraction, temperature )

flash_calculator.flash_calculation()
vars = x0 + y0

solution = fsolve(equations, vars, args = (flash_calculator))

print(f"x : {solution[:5]} \ny : {solution[5:]}")


