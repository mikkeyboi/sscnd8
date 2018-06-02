import numpy as np

def stn_ninf(V):
    ninf = 1 / (1 + np.exp(-(V + 32) / 8.0))
    return ninf

def th_hinf(V):
    hinf = 1 / (1 + np.exp((V + 41)/4))
    return hinf