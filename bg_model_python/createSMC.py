import numpy as np

def createSMC(tmax, dt, freq, cv):
    t = np.arange(0, tmax, dt); ism = 3.5
    Istim = np.zeros(t.size+1)
    deltasm = 5
    pulse = ism * np.ones(int(deltasm/dt))
    i = 1
    j = 1
    A = 1 / np.power(cv, 2)
    B = freq / A

    if cv == 0:
        instfreq = freq
    else:
        instfreq = np.random.gamma(A, B)

    ipi = 1000 / instfreq
    i = i + np.round(ipi / dt)

    timespike = []

    while i < t.size:
        timespike.append(t[int(i)])
        pulse = Istim[np.arange(i, (i + deltasm / dt - 1), dtype=int)]

        A = 1 / np.power(cv, 2)
        B = freq / A
        if cv == 0:
            instfreq = freq
        else:
            instfreq = np.random.gamma(A, B)

        ipi = 1000 / instfreq
        i = i + round(ipi / dt)
        j = j + 1
    return Istim, timespike
