def quadratic(A,B,C):
    delta = (B**2)-4*A*C
    root = {}
    if delta < 0:
        print("There is no real roots")
        return root
    elif delta == 0:
        root['root'] = (-B)/(2*A)
        return root
    else:
        root['root1'] = (-B+delta**(1/2))/(2*A)
        root['root2'] = (-B-delta**(1/2))/(2*A)
        return root
# #The following is for test only.
# #DO NOT count them as submissions
# from sys import argv
# A = float(argv[1])
# B = float(argv[2])
# C = float(argv[3])
# print(quadratic(A,B,C))
