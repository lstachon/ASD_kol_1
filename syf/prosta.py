def lineFromPoints(P, Q):
    a = Q[1] - P[1]
    b = P[0] - Q[0]
    c = a * (P[0]) + b * (P[1])

    if (b < 0):
        print("The line passing through points P and Q is:",
              a, "x ", b, "y = ", c, "\n")
    else:
        print("The line passing through points P and Q is: ",
              a, "x + ", b, "y = ", c, "\n")

    # Driver code


if __name__ == '__main__':
    P = [1, 0]
    Q = [1, 2]
    lineFromPoints(P, Q)
