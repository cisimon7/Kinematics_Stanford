from Forward import forwardKinematics


def forward_tests():
    # test cases
    # you can add more test cases here
    # angles input should be in degrees
    test_cases = [
        [0, 0, 0, 0, 0, 0],
        [-10, -50, 20, 50, 0, -60]
    ]

    for i, param in enumerate(test_cases):
        var = forwardKinematics(param)

        view = "CASE {}:\n{}\n".format(i+1, var)
        print(view)


if __name__ == '__main__':
    forward_tests()
