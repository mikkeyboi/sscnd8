import numpy as np
from createSMC import createSMC

# Time Variables
tmax = 1000  # Maximum time (ms)
dt = 0.01  # Time-step (ms)
t = np.arange(0, tmax, dt)  # t=0:dt:tmax;
n = 10  # Number of neurons in each nucleus (TH, STN, GPe, GPi)

# Initial membrane voltages for all cells
v1 = -62+np.random.rand(n, 1)*5
v2 = -62+np.random.rand(n, 1)*5
v3 = -62+np.random.rand(n, 1)*5
v4 = -62+np.random.rand(n, 1)*5
r = np.random.rand(n, 1)*2

# Sensorimotor cortex input to thalamic cells
[Istim, timespike] = createSMC(tmax, dt, 14, 0.2)



