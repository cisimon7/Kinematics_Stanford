from Forward import forwardKinematics
from math import pi
from numpy import round


def forward_tests():
    # test cases
    # you can add more test cases here
    # angles input should be in degrees
    test_cases = [
        [0, 0, 0, 0, 0, 0],
        [-10, -50, 20, 50, 0, -60],
        [60, -30, 11, -1, -1, -1]
    ]

    f_function = forwardKinematics()

    for i, param in enumerate(test_cases):
        h = f_function((
            (param[0] * pi / 180),  # q1
            (param[1] * pi / 180),  # q2
            param[2],               # d3
            (param[3] * pi / 180),  # q4
            (param[4] * pi / 180),  # q5
            (param[5] * pi / 180)   # q6
        ))

        view = f"CASE {i+1}:\n{round(h, 4)}\n"
        print(view)


if __name__ == '__main__':
    forward_tests()
