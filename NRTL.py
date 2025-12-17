import math
import copy
def calc_activity_coeff(x : list[float] , a_ij , b_ij, temperature) :
    
    alpha = [[0, 0.3, 0.424, 0, 0.3],
             [0.3, 0, 0.3, 0, 0.586],
             [0.424, 0.3, 0, 0, 0.292],
             [0, 0, 0, 0, 0],
             [0.3, 0.586, 0.292, 0, 0]]
    x = x.copy()
    a_ij = copy.deepcopy(a_ij)
    b_ij = copy.deepcopy(b_ij)
    
    x.pop(3)
    a_ij.pop(3)
    b_ij.pop(3)
    alpha.pop(3)
    for i in range(4) :
        alpha[i].pop(3)
        a_ij[i].pop(3)
        b_ij[i].pop(3)
    
    R = 1.987  # cal/mol-K
    taw = [ [0 for j in range(len(x))] for i in range(len(x))]
    g = [ [0 for j in range(len(x))] for i in range(len(x))]
    for i in range(len(x)) :
        for j in range(len(x)) :
            taw[i][j] = (a_ij[i][j] + (b_ij[i][j] * temperature)) / (R * temperature)
            g[i][j] = math.exp(- taw[i][j] * alpha[i][j])
    gamma_vec = []

    for i in range(len(x)) :
        sum1 = 0
        sum2 = 0
        sum3 = 0
        for j in range(len(x)) :
            sum1 = sum1 + (taw[j][i] * x[j] * g[j][i])
            sum2 = sum2 + (x[j] * g[j][i])
            sub1_sum3 = 0
            sub2_sum3 = 0 
            for k in range(len(x)):
                sub1_sum3 += x[k] * g[k][j]
                sub2_sum3 += taw[k][j] * x[k] * g[k][j]

            sum3 += ((x[j]*g[i][j])/ sub1_sum3) * (taw[i][j] - ((sub2_sum3) / (sub1_sum3)))
        gamma_i = (sum1 / sum2) + sum3
        gamma_vec.append(math.exp(gamma_i))
        
            
    return gamma_vec
