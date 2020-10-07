from numpy import set_printoptions
from sympy import trigsimp, lambdify
from utils import *

# Joint parameters declaration
q1, q2, d3, q4, q5, q6 = symbols("q1 q2 d3 q4 q5 q6", real=True)

# Link length initialization
l1, l2, l3 = 10, 20, 30

# Forward Kinematics Homogeneous Matrix
H = Rz(q1) * Tz(l1) * Tx(-l2) * Rx(q2) * Tz(l3) * Tz(d3) * Rz(q4) * Rx(q5) * Rz(q6)
H = trigsimp(H)

set_printoptions(suppress=True)


def forwardKinematics():
    return lambdify([(q1, q2, d3, q4, q5, q6)], H, "numpy")
