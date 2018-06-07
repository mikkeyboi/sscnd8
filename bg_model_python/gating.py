import numpy as np

def stn_ninf(V):
    ninf = 1 / (1 + np.exp(-(V + 32) / 8.0))
    return ninf

def gpe_ninf(V):
    ninf = 1 / (1 + np.exp(-(V + 50) / 14))
    return ninf

def th_hinf(V):
    hinf = 1 / (1 + np.exp((V + 41) / 4))
    return hinf

def stn_hinf(V):
    hinf = 1 / (1 + np.exp((V + 39) / 3.1))
    return hinf

def gpe_hinf(V):
    hinf = 1 / (1 + np.exp((V + 58) / 12))
    return hinf

def th_rinf(V):
    rinf = 1 / (1 + np.exp((V + 84) / 4))
    return rinf

def stn_rinf(V):
    rinf = 1 / (1 + np.exp((V + 67) / 2))
    return rinf

def gpe_rinf(V):
    rinf = 1 / (1 + np.exp((V + 70) / 2))
    return rinf

def stn_cinf(V):
    cinf = 1 / (1 + np.exp(-(V + 20) / 8))
    return cinf

def th_minf(V):
    minf = 1 / (1 + np.exp(-(V + 37) / 7))
    return minf

def stn_minf(V):
    minf = 1 / (1 + np.exp(-(V + 30) / 15))
    return minf