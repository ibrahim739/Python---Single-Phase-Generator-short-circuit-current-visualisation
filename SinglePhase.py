# This script reprents a Short circuit current calculation of a single phase generator.
# The Generator is modeled as a voltage source and a series RL branch which represents
# the internal parameters of the Generator

# ---------------------------------------------------------------------------------------------------------------------
# Brief explanation of the Single Phase short circuit calculation:
# The total fault current also known as the Asymmetrical fault current is
# composed of two components: The Ac fault current also named as
# symmetrical current or steady-state fault current + the dc offset current
# which decays exponentially with time constant taw
# In this script, we assume Maximum Dc offset which represents the worst
# case !

# --------------------------------------------------------------------------------------------------------------
# The inputs to the script are:
# V which is the Rms voltage in Volts
# L is the internal inductance in Henry
# R is the internal resistance in ohm
# f is the operating frequency in Hertz
V = input('Please enter the Rms voltage value in volts:')
L = input('Please enter the internal inductance value of the generator in Henry:')
R = input('Please enter the internal resistance value of the generator in ohm:')
f = input('Please enter the working frequency value in Hertz:')


# -----------------------------------------------------------------------------------------------------------------------
# Example Exercise ( typical input problems):
# A bolted short circuit occurs in a single phase generator with the maximum dc offset :
# V =20 kV, L = 0.0212 H, R = 0.8 Ω , F = 60 Hz.

# In this case, you enter the following parameters one by one :
# V = 20000
# L = 0.0212
# R = 0.8
# f = 60

# --------------------------------------------------------------------------------------------------------------------

# Done by Ibrahim Al-Salloum (Electrical power and machines engineer)
# if you have any other specification that you want to add to this project,
# i would be glad to do it, send me a Message on WhatsApp on: +96176537146
# or via email: ibrahimmsalloum12@gmail.com

# ---------------------------------------------------------------------------------------------------------------------


import numpy as np
import math
import matplotlib.pyplot as plt
t = np.arange(0, 3, 0.01) # You can change the time limit
                          # number whenever you want, just change the
                          # time end value ( 3 in this
                          # example)

try:
    V = float(V)
    L = float(L)
    R = float(R)
    f = float(f)
    w = 2*math.pi*f
    X = L*w
    taw = L/R
    Iac_rms = V/math.sqrt(X**2+R**2)
    Ish = dict()
    Irms = dict()
    Idc = dict()
    iter = 0
    while iter < len(t):
        Ish[iter] = abs(math.sqrt(2) * Iac_rms * math.sin(w*t[iter]-180/2) - math.sqrt(2) * Iac_rms * math.sin(-180/2) * math.exp(-t[iter]/taw))
        Idc[iter] = math.sqrt(2) * Iac_rms * math.exp(-1*t[iter]/taw)
        Irms[iter] = math.sqrt(Iac_rms**2 + Idc[iter]**2)
        iter = iter + 1
    Iac_rms = Iac_rms * np.ones(len(t))
    plt.plot(t,Ish.values(), label = 'Iassymetrical(total)-instantaneous')
    plt.plot(t,Irms.values(), label = 'Iassymetrical(total)-rms')
    plt.plot(t,Iac_rms, label = 'Iac-rms')
    plt.plot(t,Idc.values(), label = 'Idc')
    plt.xlabel('Time in seconds')
    plt.ylabel('Short circuit current in Ampere')
    plt.title('Singe Phase Short circuit current')
    plt.legend()
    plt.grid()
    plt.show()
except:
    print('Please enter valid integer numbers for the specified values')
