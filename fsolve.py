from Bubble_T_Flash import BubbleTFlash


def equations(vars, flash: BubbleTFlash ):
    x = vars[:5]
    y = vars[5:]

    k = flash.vle_system.calculate_k_value(x, flash.temperature)

    F = flash.vle_system.inlet_flow
    V = F * flash.vapor_fraction
    L = F - V
    z = flash.vle_system.composition

    eqs = []

    # Phase equilibrium
    for i in range(5):
        eqs.append(y[i] - k[i]*x[i])

    # Component balances (first 4)
    for i in range(4):
        eqs.append(F*z[i] - L*x[i] - V*y[i])

    # Normalization
    eqs.append(sum(x) - 1.0)

    return eqs
    