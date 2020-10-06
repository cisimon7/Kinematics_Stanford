from math import pi
from sympy import trigsimp, lambdify
from utils import *
from numpy import round

# Joint parameters declaration
q1, q2, d3, q4, q5, q6 = symbols("q1 q2 d3 q4 q5 q6", real=True)

# Link length initialization
l1, l2, l3 = 10, 20, 30

# Forward Kinematics Homogeneous Matrix
H = Rz(q1) * Tz(l1) * Tx(-l2) * Rx(q2) * Tz(l3) * Tz(d3) * Rz(q4) * Rx(q5) * Rz(q6)
H = trigsimp(H)


def forwardKinematics(params):
    f = lambdify([(q1, q2, d3, q4, q5, q6)], H, "numpy")
    h = f((
        (params[0] * pi / 180),  # q1
        (params[1] * pi / 180),  # q2
        params[2],  # d3
        (params[3] * pi / 180),  # q4
        (params[4] * pi / 180),  # q5
        (params[5] * pi / 180)  # q6
    ))

    return round(h, 4)
